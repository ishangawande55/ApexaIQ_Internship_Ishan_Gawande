import requests

def fetch_openlibrary_data(isbns):
    """
    Fetch book data from OpenLibrary API for given ISBNs.

    :param isbns: List of ISBN numbers
    :return: JSON response as dictionary
    """
    base_url = "https://openlibrary.org/api/books"
    query = ",".join([f"ISBN:{isbn}" for isbn in isbns])
    params = {"bibkeys": query, "format": "json"}

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"API request failed with status {response.status_code}"}
    
    