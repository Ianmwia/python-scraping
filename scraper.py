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

#4. get price and name
product_name = soup2.find_all('h3', class_='name')

product_price = soup2.find_all('div', class_='prc')

#print(product_name)
#print(product_price)

#save in a list
products = []

for i in range(len(product_name)):
    p_name = product_name[i].get_text(strip=True)
    p_price = product_price[i].get_text(strip=True)

    products.append([p_name, p_price])

print(products)

#5. save
save_input = input('Want to save the products "yes" or "no: ')
def save_or_not():
    if save_input == "yes":
        save_file_as = input('Enter a filename: ')
        with open(save_file_as, 'w') as file:
            for name, price in products:
                file.write(f'{name} : {price}\n')
        print(f'Your file has been saved as {save_file_as}')

    else:
        print('No file to be saved')
save_or_not()

