import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd

# URL of the page to scrape
url = "https://quotes.toscrape.com/"

# Define headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

# Make an HTTP GET request to the URL with headers
response = requests.get(url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract and print quotes
quotes = soup.find_all("span", class_="text")
for quote in quotes:
    print(quote.text)

# Extract and print authors
authors = soup.find_all("small", class_="author")
for author in authors:
    print(author.text)

quote_texts = [quote.text for quote in quotes]
author_names = [author.text for author in authors]

data = {
    "Quote": quote_texts,
    "Author": author_names
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("quotes.csv", index=False, encoding='utf-8')

# Sleep for a random interval between 1 and 3 seconds
s = random.uniform(1, 3)
print(f"Sleeping for {s:.2f} seconds")
time.sleep(s)