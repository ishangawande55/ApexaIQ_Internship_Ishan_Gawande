import pytest
import time
from unittest.mock import patch
from src.api_client import fetch_api_data

# Mock API response for successful requests
MOCK_SUCCESS_RESPONSE = {
    "userId": 1,
    "id": 1,
    "title": "Mocked API Response",
    "completed": False
}

# Mock API response for failed requests
MOCK_ERROR_RESPONSE = {
    "error": "Internal Server Error"
}

# Mock API response with missing keys
MOCK_MISSING_KEYS_RESPONSE = {
    "userId": 1,
    "id": 1,
    "completed": False
}


@patch("requests.get")
def test_fetch_api_data(mock_get):
    """Test API response for a successful request."""
    
    # Mock the API response
    mock_get.return_value.json.return_value = MOCK_SUCCESS_RESPONSE
    
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = fetch_api_data(url)
    
    # Assertions
    assert isinstance(response, dict), "Response should be a dictionary"
    assert "id" in response, "Response should contain 'id' key"
    assert response["id"] == 1, "ID should be 1"
    assert response["title"] == "Mocked API Response", "Title should match"
    assert response["completed"] is False, "Completed should be False"


@patch("requests.get")
def test_api_failure(mock_get):
    """Test API failure scenario (500 Internal Server Error)."""
    
    # Mock API failure
    mock_get.return_value.status_code = 500
    mock_get.return_value.json.return_value = MOCK_ERROR_RESPONSE
    
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = fetch_api_data(url)
    
    # Assertions
    assert isinstance(response, dict), "Response should be a dictionary"
    assert "error" in response, "Response should contain 'error' key"
    assert response["error"] == "Internal Server Error", "Error message should match"


@patch("requests.get")
def test_missing_keys(mock_get):
    """Test API response with missing keys."""
    
    # Mock API response with missing 'title' key
    mock_get.return_value.json.return_value = MOCK_MISSING_KEYS_RESPONSE
    
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = fetch_api_data(url)
    
    # Assertions
    assert isinstance(response, dict), "Response should be a dictionary"
    assert "title" not in response, "Response should not contain 'title' key"
    assert "userId" in response, "Response should contain 'userId' key"
    assert "id" in response, "Response should contain 'id' key"


@patch("requests.get")
def test_response_time(mock_get):
    """Test if API response time is within acceptable limits."""
    
    # Mock API response
    mock_get.return_value.json.return_value = MOCK_SUCCESS_RESPONSE
    
    url = "https://jsonplaceholder.typicode.com/todos/1"
    
    # Measure time taken to get response
    start_time = time.time()
    response = fetch_api_data(url)
    end_time = time.time()
    
    response_time = end_time - start_time
    
    # Assertions
    assert response_time < 1.0, f"API response took too long: {response_time:.2f} seconds"
    assert isinstance(response, dict), "Response should be a dictionary"
    assert "id" in response, "Response should contain 'id' key"
    assert response["id"] == 1, "ID should be 1"