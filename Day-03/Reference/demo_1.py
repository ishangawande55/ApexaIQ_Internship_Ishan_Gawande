from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the target webpage
driver.get("https://en.wikipedia.org/wiki/Java_version_history")  # Replace with the actual URL
time.sleep(2)  # Allow some time for the page to load

# Locate all tables on the page
tables = driver.find_elements(By.TAG_NAME, "table")

# List to store all DataFrames
dfs = []

# Iterate through each table
for index, table in enumerate(tables):
    rows = table.find_elements(By.XPATH, ".//tr")
    
    # Extract the header (column names)
    header = []
    header_columns = rows[0].find_elements(By.XPATH, ".//th") if rows else []
    for col in header_columns:
        header.append(col.text.strip())
    
    # Create a list to store rows of data
    table_data = []
    
    # Iterate through each row in the table, starting from the second row
    for row in rows[1:]:
        row_data = []
        columns = row.find_elements(By.XPATH, ".//td")
        
        # Extract text from each column in the row
        for col in columns:
            row_data.append(col.text.strip())
        
        # Only append non-empty rows to the list
        if row_data:
            table_data.append(row_data)
    
    # Ensure headers match data length
    if table_data and header:
        df = pd.DataFrame(table_data, columns=header)
    else:
        df = pd.DataFrame(table_data)
    
    # Add a column to indicate table index
    df.insert(0, "Table_Index", index + 1)
    
    # Append DataFrame to the list
    dfs.append(df)

# Concatenate all DataFrames into one
final_df = pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()

# Save DataFrame to CSV if it's not empty
if not final_df.empty:
    final_df.to_csv("scraped_tables.csv", index=False)
    print(final_df)
else:
    print("No tables found or extracted.")

# Close the WebDriver
driver.quit()