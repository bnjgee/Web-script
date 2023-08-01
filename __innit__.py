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
parent_elements = soup.find_all('div', class_='sphinx-tabs docutils container')

for parent_element in parent_elements:
    caption_element = parent_element.find('span', class_='caption-text')
    versions_elements = parent_element.find_all('button', class_='sphinx-tabs-tab')
    div_highlight = parent_element.find_all('div', class_='highlight')
    pre_elements = parent_element.find_all('pre')

    
    if caption_element:
        caption_text = caption_element.get_text()
        print("Caption:", caption_text)

    if versions_elements:

        for pre_element in div_highlight:
            vamos_elements = pre_element.find_all('span', class_='go')
            print(vamos_elements)
        
        for versions_element in versions_elements:
            version_text = versions_element.get_text()
            print("Version:", version_text)

            
            for pre_elemento in vamos_elements:
                vamos_text = pre_elemento.get_text()
                print("Go:", vamos_text)
    """         
        for versions_element in versions_elements:
            version_text = versions_element.get_text()
            print("Version:", version_text)

            for pre_elemento in vamos_elements:
                vamos_text = pre_elemento.get_text()
                print("Go:", vamos_text)

    
    print()
       
    else:

        for go_element in go_elements:
            go_text = go_element.get_text()
            print("Go:", go_text)  


    
    """

