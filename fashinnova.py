import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import urllib.request

dir_path = os.path.dirname(os.path.realpath(__file__))
baseurl = 'https://www.fashionnova.com'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}

cat_link = [['https://www.fashionnova.com/collections/dresses','Women'],
         ['https://www.fashionnova.com/collections/mens', 'Men']]

for cat in cat_link[1:]:
    r = requests.get(cat[0], headers=headers)
    soup = BeautifulSoup(r.content, "lxml")

    product_list = soup.find_all("form", class_="variants add-to-cart-form product-info-json")
    products_final_processed_list = []
    for product in product_list:
        full_name = product["data-product-title"].replace('/',' ')
        price = "$"+product["data-product-price"]
        image_div = (product.find('div', class_="mediabox"))
        print(image_div)
        image_url = "https:"+image_div.find('img')['data-src']
        print(image_url)

        my_path = f'\\images\\fashionnova\\{cat[1]}'  # use whatever path you like
        file_path = dir_path + my_path
        urllib.request.urlretrieve(image_url,
                                   os.path.join(file_path, os.path.basename((full_name + '.jpg'))))

        product = {
            'Name': full_name,
            'Category': cat[1],
            'Price': price,
            'Image URL': image_url,
       }
        products_final_processed_list.append(product)

    df = pd.DataFrame(products_final_processed_list, columns=['Name', 'Category', 'Price', 'Image URL'])
    df.to_excel(dir_path + f"\\images\\fashionnova\\fashionnova_{cat[1]}.xlsx", index=False)

