"""Java Version Scraper"""

# Import libraries
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

# Navigate to the Wikipedia page
driver.get("https://en.wikipedia.org/wiki/Java_version_history")
time.sleep(1)

# Locate the table on the page
table = driver.find_element(By.CLASS_NAME, "wikitable")
rows = table.find_elements(By.XPATH, ".//tr")

# Extract the header (column names)
header = []
header_columns = rows[0].find_elements(By.XPATH, ".//th")
for col in header_columns:
    header.append(col.text.strip())

# Create a list to store rows of data
java_versions = []

# Iterate through each row in the table, starting from the second row
for row in rows[1:]:
    row_data = []
    columns = row.find_elements(By.XPATH, ".//td")
    
    # Extract text from each column in the row
    for col in columns:
        row_data.append(col.text.strip())
    
    # Only append non-empty rows to the list
    if row_data:
        java_versions.append(row_data)

# Create a DataFrame from the extracted data, using the header as column names
df = pd.DataFrame(java_versions, columns=header)

# Save DataFrame to CSV
df.to_csv("java_versions.csv", index=False)

# Output the DataFrame
print(df)

# Close the WebDriver
driver.quit()