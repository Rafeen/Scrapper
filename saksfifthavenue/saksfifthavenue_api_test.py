from bs4 import BeautifulSoup
import requests
import json
import re
import time
from text_file_generator import text_file_generator
from clarifai.clarifai_connector import upload_to_clarifai
from google.protobuf.struct_pb2 import Struct

base_url = "https://www.saksfifthavenue.com"
REGEX_URL_VIEW = "(view)=\d+"
REGEX_URL_NAO = "(Nao)=\d+"

image_counter = 0
product_counter = 0
page_counter = 0
elapsed_scraping_time = 0.0
elapsed_uploading_time = 0.0

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}

try:
    for page in range(0,70):
        url = "https://www.saksfifthavenue.com/Women-s-Apparel/shop/_/N-52flog/Ne-6lvnb5?Nao=0"

        url = re.sub(REGEX_URL_NAO, f'Nao={page*150}', url)

        scrap_start = time.time()

        response = requests.get(url, headers=headers)
        time.sleep(5)

        soup = BeautifulSoup(response.content, "lxml")

        products_list = soup.find_all("div", class_="pa-product-large sfa-pa-product-with-swatches")

        scrap_end = time.time()
        elapsed_scraping_time += scrap_end-scrap_start

        if len(products_list) == 0:
            print(f"no products on page={page}")
            break

        else:
            print(url)
            print(len(products_list))

        for product in products_list:
            product_counter += 1

            brand = product.find("span", class_="product-designer-name").text.strip()
            name = product.find("p", class_="product-description").text.strip()
            product_url = product.find("a", class_="mainBlackText")["href"]

            if product.find("span", class_="product-price") is not None:
                if product.find("span", class_="product-price").text:
                    pre_price = product.find("span", class_="product-price").text
                    pre_price = pre_price.split()
                    price = float(round(float(pre_price[-1]) / 92.908))
                else:
                    price = "Not Available"
            else:
                print(f"did not upload {name}")
                continue

            input_metadata = Struct()
            image_metadata = {"name": name, "brand": brand, "price": price, "url": product_url}
            input_metadata.update(image_metadata)

            images = []
            image_main = product.find("img", {"alt" : "Product image"})["src"].replace("247x329", "566x755")
            images.append(image_main)

            image_alternative = product.find("img", {"alt" : "Product image"})["params"]
            image_alternative = image_alternative.split(',')
            if len(image_alternative) > 1:
                image_alternative = image_alternative[1].replace("247x329", "566x755")
                images.append(image_alternative)

            for image in images:
                image_url = image
                upload_start = time.time()
                value = upload_to_clarifai(input_metadata=input_metadata, image_url=image_url,
                                           image_counter=image_counter)
                upload_end = time.time()
                elapsed_uploading_time += upload_end - upload_start
                image_counter = value
                if page_counter > 0 and image_counter % 100 == 0:
                    print("another 100 done to clarifai")

        print(f"uploaded={image_counter}, products_url={len(products_list)} products_total={product_counter} page_counter={page}")
        page_counter=page


finally:
    elapsed_uploading_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_uploading_time))
    elapsed_scraping_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_scraping_time))
    text = f"uploaded={image_counter}, products={product_counter} page={page_counter} category=Women Apparel shop all uploading_time={elapsed_uploading_time} scraping_time={elapsed_scraping_time}"
    filename = "saksfifthavenue_data_report"
    text_file_generator(filename, text)
    print(text)