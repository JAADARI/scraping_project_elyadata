from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient
import httpx

app = FastAPI()


# Replace 'YOUR_ACCESS_TOKEN' with the actual access token obtained from the Facebook Developer portal
ACCESS_TOKEN = 'EAAQIvulOqQ0BOwOlKYMipkoxArJazFw9uBejxVC4AQTxidziHapyEIhELMpHdRbQrvuglZBAkMjRZAsqShu1PuGAI7NOzmNDeln2t2XTuTBwMIBLCiZAdvziZBbdIaBXIbKT7GWIYj1dBHX8EGZC6hziQCmLs0WLExK3BLP2Gp3VxCEioYFZCRBePG9x5cTnfLsaJtVGO4pDcO4sbuDAq4eJMbnZAI0DgNPQT5eXF1jodSOJdXkZBEZBZAiujquy1sjwZDZD'
MONGODB_URI = "mongodb://localhost:27017/scraping_db"

mongodb_client = AsyncIOMotorClient(MONGODB_URI)
db = mongodb_client["scraping_db"]
collection = db["facebook_data"]

async def scrape_facebook_data(page_id: str):
    api_url = f'https://graph.facebook.com/v18.0/{page_id}/'
    fields = 'email,name,first_name,last_name,middle_name,short_name,name_format,picture'  # Example fields
    params = {
        'access_token': ACCESS_TOKEN,
        'fields': fields  # Add this line to include additional fields
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = [post['message'] for post in data.get('data', []) if 'message' in post]
                # Print the posts
        print("Posts:",len(posts),"data",len(data),data)
        for post in posts:
            print(post)
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

@app.get("/scrape-facebook/{page_id}")
async def scrape_facebook(page_id: str):

    try:
        scraped_data = await scrape_facebook_data(page_id)

        if scraped_data:
            # Save the data to MongoDB
            await collection.insert_one({"page_id": page_id, "posts": scraped_data})

            return JSONResponse(content=jsonable_encoder({"message": "Scraping successful", "data": scraped_data}))
        else:
            return JSONResponse(content=jsonable_encoder({"message": "Scraping failed"}), status_code=500)
    except HTTPException as http_ex:
        # Handle HTTP exceptions from the scraping function
        return JSONResponse(content=jsonable_encoder({"message": str(http_ex.detail)}), status_code=http_ex.status_code)
    except Exception as e:
        # Handle other exceptions, such as database connection issues
        return JSONResponse(content=jsonable_encoder({"message": str(e)}), status_code=500)

