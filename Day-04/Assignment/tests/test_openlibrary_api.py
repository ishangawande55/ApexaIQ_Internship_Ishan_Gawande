import pytest
from src.api_client1 import fetch_openlibrary_data


def test_fetch_openlibrary_data_valid_isbn():
    """Test API response with a valid ISBN."""
    valid_isbn = ["0201558025"]
    response = fetch_openlibrary_data(valid_isbn)
    
    # Assertions
    assert isinstance(response, dict), "Response should be a dictionary"
    assert "ISBN:0201558025" in response, "Response should contain the requested ISBN"
    assert "info_url" in response["ISBN:0201558025"], "Info URL should be present"
    assert "preview_url" in response["ISBN:0201558025"], "Preview URL should be present"


def test_fetch_openlibrary_data_empty_isbn():
    """Test API response with an empty ISBN list."""
    empty_isbn = []
    response = fetch_openlibrary_data(empty_isbn)
    
    # Assertions
    assert isinstance(response, dict), "Response should be a dictionary"
    assert response == {}, "Response should be empty for an empty ISBN list"


def test_fetch_openlibrary_data_multiple_valid_isbns():
    """Test API response with multiple valid ISBNs."""
    valid_isbns = ["0201558025", "9780131103627"]  # Adding another valid ISBN
    response = fetch_openlibrary_data(valid_isbns)
    
    # Assertions
    assert isinstance(response, dict), "Response should be a dictionary"
    assert "ISBN:0201558025" in response, "First valid ISBN should be present in the response"
    assert "ISBN:9780131103627" in response, "Second valid ISBN should be present in the response"
    assert all("info_url" in response[isbn] for isbn in response), "Each book should contain an info_url"
