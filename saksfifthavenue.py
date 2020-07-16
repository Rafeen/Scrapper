import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import urllib.request

dir_path = os.path.dirname(os.path.realpath(__file__))
baseurl = 'https://www.saksfifthavenue.com'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}

cat_link = [['https://www.saksfifthavenue.com/Women-s-Apparel/shop/_/N-52flog/Ne-6lvnb5','Women'],
         ['https://www.saksfifthavenue.com/Shoes/shop/_/N-52k0s7/Ne-6lvnb5', 'Shoes']]

for cat in cat_link:
    r = requests.get(cat[0], headers=headers)
    soup = BeautifulSoup(r.content, "lxml")

    product_list = soup.find_all("div", class_="pa-product-large sfa-pa-product-with-swatches")
    products_final_processed_list = []
    for product in product_list[0:60]:
        brand_name = product.find("span", class_="product-designer-name").text.strip()
        product_name = product.find("p", class_="product-description").text.strip()
        full_name = brand_name + " " + product_name
        if product.find("span", class_="product-price").text:
            price = product.find("span", class_="product-price").text
        else:
            price = "None/Gift"
        image_tags = product.find_all("img", {"alt" : "Product image"})
        image_url = ""
        for image in image_tags:
            image_url = image["src"].replace("247x329", "566x755")
        print(image_url)

        my_path = f'\\images\\saksfifthavenue\\{cat[1]}'  # use whatever path you like
        file_path = dir_path + my_path
        # urllib.request.urlretrieve(image_url,
        #                            os.path.join(file_path, os.path.basename((full_name + '.jpg'))))

        product = {
            'Name': full_name,
            'Category': cat[1],
            'Price': price,
            'Image URL': image_url,
       }
        products_final_processed_list.append(product)

    df = pd.DataFrame(products_final_processed_list, columns=['Name', 'Category', 'Price', 'Image URL'])
    df.to_excel(dir_path + f"\\saksfifthavenue_{cat[1]}.xlsx", index=False)