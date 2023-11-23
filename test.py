from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_scrape_facebook():
    # Replace 'id' with the actual Facebook page ID you want to test
    response = client.get("/scrape-facebook/3583642901952386")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains the expected message
    assert response.json()["message"] == "Scraping successful"

    # Add more assertions based on your specific requirements
    # For example, you can check if the returned data structure is as expected
    assert "data" in response.json()
    assert "email" in response.json()["data"]
    assert "first_name" in response.json()["data"]
    assert "last_name" in response.json()["data"]
    assert "short_name" in response.json()["data"]
    assert "name_format" in response.json()["data"]



