import requests

def fetch_api_data(url):
    """Fetch data from API and return JSON response."""
    response = requests.get(url)
    return response.json()