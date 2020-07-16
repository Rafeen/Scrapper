import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import urllib.request

dir_path = os.path.dirname(os.path.realpath(__file__))
baseurl = 'https://www.macys.com'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}

r = requests.get('https://www.macys.com/shop/womens-clothing/womens-sale-clearance/Price_discount_range/20_PERCENT_%20off%20%26%20more?id=10066&tagid=4273177_01_02&ctype=G&cm_re=2020.07.14-_-HOMEPAGE_INCLUDE_1_row_01-_-CATEGORY%20--%205125%20--%20:women',headers=headers)
soup = BeautifulSoup(r.content, "lxml")


product_list = soup.find_all("li", class_="cell productThumbnailItem")
product_links = []

for item in product_list:
    for link in item.find_all('a', href=True):
        product_links.append(baseurl + link['href'])
product_links = list(set(product_links))
print('\n'.join(map(str, product_links)))

products_final_processed_list = []
for link in product_links:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")

    brand_name = (soup.find('h4', class_='p-brand-title bold').text.strip())
    product_name = (soup.find('h1', class_='p-name').text.strip())
    full_name = brand_name + " " + product_name
    full_name = full_name.replace(',', '')
    pre_processed_price = (soup.find('div', class_='price').text.strip())
    price = pre_processed_price.replace('Reg.', '')
    price = price.replace('Orig.', '')
    image_lines = (soup.find('li', class_='main-img swiper-slide'))
    image_url = image_lines.find('img')['src']

    product = {
        'Name': full_name,
        'Category': 'Women',
        'Price': price,
        'Image URL': image_url,
    }

    my_path = f'\\images\\macys\\{product["Category"]}'  # use whatever path you like
    file_path = dir_path + my_path
    urllib.request.urlretrieve(product["Image URL"], os.path.join(file_path, os.path.basename((product["Name"] + '.jpg'))))

    products_final_processed_list.append(product)


# df = pd.DataFrame(products_final_processed_list, columns= ['Name', 'Category', 'Price', 'Image URL'])
# print(df)
#
#
#
# df.to_excel(dir_path + "\\macys_women.xlsx", index=False)


