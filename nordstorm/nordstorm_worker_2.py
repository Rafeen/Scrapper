import requests
import json
import re
import time
from text_file_generator import text_file_generator
from clarifai.clarifai_connector import upload_to_clarifai
from google.protobuf.struct_pb2 import Struct
from nordstorm.header import headers

base_url = "https://www.nordstrom.com"

REGEX_URL_COUNT = "(top)=\d+"
REGEX_URL_OFFSET = "(offset)=\d+"

image_counter = 0
product_counter = 0
page_counter = 0

elapsed_scraping_time = 0.0
elapsed_uploading_time = 0.0

try:
    for page in range(1, 3):
        scrap_start = time.time()
        url = "https://www.nordstrom.com/api/browse/browse/women/jewelry?offset=0&top=5000"

        if page > 1:
            url = re.sub(REGEX_URL_OFFSET, f'page={page}', url)
            page_counter = page
        #
        # elif page == 2:
        #     url = "https://www.nordstrom.com/api/browse/browse/women/clothing?top=72&breadcrumb=Home%2FWomen%2FClothing&origin=topnav&offset=3&page=2"

        payload = "<file contents here>"

        response = requests.get(url, headers=headers)
        while response.status_code != 200:
            response = requests.get(url, headers=headers)
            print(response.status_code)
            print("retrying after 5 sec")
            print(url)
            time.sleep(5)
            print("5 sec done")

        # if response.status_code != 200:
        #     print(response.status_code)
        #     print(url)
        #     break

        if response.status_code == 200:
            print(response.status_code)
            print(url)
        json_data = json.loads(response.text.encode('utf8'))

        scrap_end = time.time()
        elapsed_scraping_time += scrap_end-scrap_start

        if len(json_data['productsById']) == 0:
            print("no products")
            break
        else:
            print(len(json_data['productsById']))
        for product_id in json_data['productsById']:
            product_counter += 1

            name = json_data['productsById'][product_id]["name"]
            brand = json_data['productsById'][product_id]['brandName']
            colors = ', '.join(json_data['productsById'][product_id]['colorIds'])
            product_url = base_url + json_data['productsById'][product_id]['productPageUrl']
            price = json_data['productsById'][product_id]["pricesById"]["original"]["minItemPrice"]

            input_metadata = Struct()
            image_metadata = {"name": name, "brand": brand, "price": price, "url": product_url}
            input_metadata.update(image_metadata)

            for media_id in json_data['productsById'][product_id]['mediaById']:
                if json_data['productsById'][product_id]['mediaById'][media_id]['group'] == "main":
                    image_url = json_data['productsById'][product_id]['mediaById'][media_id]['src']
                    upload_start = time.time()
                    value = upload_to_clarifai(input_metadata=input_metadata, image_url=image_url, image_counter=image_counter)
                    upload_end = time.time()
                    elapsed_uploading_time += upload_end-upload_start
                    image_counter = value
                    if image_counter%2000==0:
                        print("uploaded another 2000")
        print(f"uploaded={image_counter}, products={product_counter} page={page_counter}")


finally:
    elapsed_uploading_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_uploading_time))
    elapsed_scraping_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_scraping_time))
    text = f"uploaded={image_counter}, products={product_counter} page={page_counter} category=Women Jewelery uploading_time={elapsed_uploading_time} scraping_time={elapsed_scraping_time}"
    filename = "nordstorm_data_report"
    text_file_generator(filename, text)
    print(text)







