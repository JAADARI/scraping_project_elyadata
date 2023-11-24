from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_scrape_facebook():
    id=3583642901952386
    access_token="EAAQIvulOqQ0BO6nJPNQwLdb9b7gx0f4YfaxyZCU729IZBXsFPU8ZByuP7Bd1Mp712fImNPPPphuGTqq25BYsH5ZBpU8VBUWfvWOEFa1r61ZCKXL0idBCQc7ZBc1wN00wqLQViZAI1ecTfUH1uptXQk43kri1GHVjjSVogJgux7f4lCv2bR7PB7KtPDZADFjzNEP6EUxOCKwZCnp6U3zCDjF3GVJ8leu7op6AnsOxHCtYdxASYEqjJZC1QOPrdHA6v12QZDZD"
    # Replace 'id' with the actual Facebook page ID you want to test
    response = client.get(f"/scrape-facebook/{id}?access_token={access_token}")

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



