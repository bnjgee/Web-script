import requests
from bs4 import BeautifulSoup
import re

url = 'https://greenbone.github.io/docs/latest/22.4/source-build/index.html#id6'  # Replace this with the URL of the website you want to extract from

# Send an HTTP GET request to fetch the webpage's content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    content = response.text
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(content, 'html.parser')

# Find all elements with class="parent"
parent_elements = soup.find_all('div', class_='highlight')

print(parent_elements)
