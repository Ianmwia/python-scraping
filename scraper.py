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

#2. store in pair
categories = {}

for url in category_url:
    split_name = url.split('.ke')[1].split('/')[1]
    categories[split_name] = url
#print(categories)

#3. list of products and prices
user_input_product = input(f'select a jumia product key to scrape from {list(categories.keys())}: ')

product_price_url = categories.get(user_input_product)
print(product_price_url)

response2 = requests.get(product_price_url, headers=headers)
soup2 = BeautifulSoup(response.text, 'html.parser')

