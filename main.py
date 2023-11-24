from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient
import httpx

app = FastAPI()
print("Now the Server is Running")

ACCESS_TOKEN = 'EAAQIvulOqQ0BO6nJPNQwLdb9b7gx0f4YfaxyZCU729IZBXsFPU8ZByuP7Bd1Mp712fImNPPPphuGTqq25BYsH5ZBpU8VBUWfvWOEFa1r61ZCKXL0idBCQc7ZBc1wN00wqLQViZAI1ecTfUH1uptXQk43kri1GHVjjSVogJgux7f4lCv2bR7PB7KtPDZADFjzNEP6EUxOCKwZCnp6U3zCDjF3GVJ8leu7op6AnsOxHCtYdxASYEqjJZC1QOPrdHA6v12QZDZD'
MONGODB_URI = "mongodb://mongo:27017/scraping_db"

mongodb_client = AsyncIOMotorClient(MONGODB_URI)
db = mongodb_client["scraping_db"]
collection = db["facebook_data"]

async def scrape_facebook_data(page_id: str,access_token: str):
    api_url = f'https://graph.facebook.com/v18.0/{page_id}/'
    fields = 'email,name,first_name,last_name,middle_name,short_name,name_format,picture'  # Example fields
    params = {
        'access_token': access_token,
        'fields': fields  # Add this line to include additional fields
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

@app.get("/scrape-facebook/{page_id}")
async def scrape_facebook(page_id: str,access_token: str):

    try:
        scraped_data = await scrape_facebook_data(page_id,access_token)

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

