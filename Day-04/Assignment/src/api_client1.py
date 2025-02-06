import requests

def fetch_openlibrary_data(isbns):
    """
    Fetch book data from Open Library API.
    :param isbns: List of ISBN numbers
    :return: Dictionary containing book details
    """
    base_url = "https://openlibrary.org/api/books"
    bibkeys = ",".join([f"ISBN:{isbn}" for isbn in isbns])
    params = {
        "bibkeys": bibkeys,
        "format": "json"
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {}
