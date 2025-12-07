import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.jumia.co.ke'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

product_pages = {
    'electronics': 'https://www.jumia.co.ke/electronics/',
    'appliances': 'https://www.jumia.co.ke/home-office-appliances/',
    'gaming': 'https://www.jumia.co.ke/video-games/',
    'computing': 'https://www.jumia.co.ke/computing/'
}

#select product
user_input = input(f'select a jumia product key to scrape from {list(product_pages.keys())}: ')
#product_url = product_pages.values()
product_url = product_pages.get(user_input)
print(product_url)

#scrape to get categories
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
response = requests.get(product_url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())

categories = []

#1.find the href
category_url = []
jumia_href = soup.find_all('div', class_='_6c-shs') # use a unique selector if the first is common 
#print(jumia_href)
if jumia_href:
    for div in jumia_href:
        for link in div.find_all('a', href=True):
            category_href = link['href']
            category_url.append(category_href)
print(category_url)

#2. 

# browse by category
#select_a_category = input(f'select a category in the products page to scrape from: ')

#scraping
response = requests.get(BASE_URL, headers=headers)
#print(response)