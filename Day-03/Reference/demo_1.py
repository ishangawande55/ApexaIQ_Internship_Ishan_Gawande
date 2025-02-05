import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage
url = "https://en.wikipedia.org/wiki/Java_version_history"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all tables on the page
    tables = soup.find_all("table")
    
    # List to store all data from all tables
    all_table_data = []
    header = None  # Will hold the header from the first table
    
    # Iterate through each table
    for table in tables:
        rows = table.find_all("tr")  # Find all rows in the table
        
        # Extract headers (column names) if available
        table_header = []
        headers = rows[0].find_all("th")
        for header_cell in headers:
            table_header.append(header_cell.get_text(strip=True))
        
        # If header is not already defined, assign the first table header to all
        if not header:
            header = table_header
        
        # Extract rows of data
        table_data = []
        for row in rows[1:]:  # Skip the first row (header)
            row_data = []
            columns = row.find_all("td")
            
            for col in columns:
                row_data.append(col.get_text(strip=True))
                
            # Only append non-empty rows to the list
            if row_data:
                table_data.append(row_data)
        
        # Append the table's data to the overall list
        all_table_data.extend(table_data)
    
    # Create a DataFrame from all collected table data
    if all_table_data:
        df = pd.DataFrame(all_table_data, columns=header if header else ["Column" + str(i) for i in range(len(all_table_data[0]))])
        # Save all tables data to a single CSV file
        df.to_csv("all_java_tables.csv", index=False)
        print("All tables saved to 'all_java_tables.csv'")
else:
    print(f"Failed to retrieve webpage. Status code: {response.status_code}")