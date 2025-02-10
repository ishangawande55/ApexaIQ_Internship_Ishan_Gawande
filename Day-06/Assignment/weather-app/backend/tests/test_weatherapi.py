import os
import pytest
from fastapi.testclient import TestClient
from main import app
from .test_weather_data import test_weather_data

# Create a test client
client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def set_env():
    """Set environment variables for testing."""
    os.environ["OPENWEATHER_API_KEY"] = "test_api_key"

def test_home():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Weather API is running!"}

def test_weather_valid_request(monkeypatch):
    """Test /weather endpoint with valid latitude and longitude."""

    def mock_get(*args, **kwargs):
        """Mock the requests.get response."""
        class MockResponse:
            status_code = 200
            def json(self):
                return test_weather_data  # Use imported mock data
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    response = client.get("/weather?lat=40.7128&lon=-74.0060")
    assert response.status_code == 200

    json_data = response.json()

    # Validate structured response
    assert json_data["location"] == test_weather_data["name"]
    assert json_data["country"] == test_weather_data["sys"]["country"]

    assert "temperature" in json_data
    assert json_data["temperature"]["current"] == test_weather_data["main"]["temp"]
    assert json_data["temperature"]["feels_like"] == test_weather_data["main"]["feels_like"]
    assert json_data["temperature"]["min"] == test_weather_data["main"]["temp_min"]
    assert json_data["temperature"]["max"] == test_weather_data["main"]["temp_max"]

    assert "humidity" in json_data
    assert json_data["humidity"] == test_weather_data["main"]["humidity"]

    assert "pressure" in json_data
    assert json_data["pressure"] == test_weather_data["main"]["pressure"]

    assert "wind" in json_data
    assert json_data["wind"]["speed"] == test_weather_data["wind"]["speed"]
    assert json_data["wind"]["gust"] == test_weather_data["wind"]["gust"]
    assert json_data["wind"]["direction"] == test_weather_data["wind"]["deg"]

    assert "cloudiness" in json_data
    assert json_data["cloudiness"] == f"{test_weather_data['clouds']['all']}%"

    assert "visibility" in json_data
    assert json_data["visibility"] == f"{test_weather_data['visibility'] / 1000} km"

    assert "weather" in json_data
    assert json_data["weather"]["main"] == test_weather_data["weather"][0]["main"]
    assert json_data["weather"]["description"] == test_weather_data["weather"][0]["description"]
    assert json_data["weather"]["icon"] == f"http://openweathermap.org/img/wn/{test_weather_data['weather'][0]['icon']}.png"

def test_weather_missing_api_key(monkeypatch):
    """Test /weather endpoint when API key is missing."""

    monkeypatch.delenv("OPENWEATHER_API_KEY", raising=False)
    
    response = client.get("/weather?lat=40.7128&lon=-74.0060")
    assert response.status_code == 400
    assert response.json() == {"detail": "Missing API Key"}

def test_weather_invalid_params():
    """Test /weather endpoint with missing parameters."""
    response = client.get("/weather")
    assert response.status_code == 422  # Unprocessable entity due to missing query params