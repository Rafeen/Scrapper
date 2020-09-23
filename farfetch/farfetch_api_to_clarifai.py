import requests
import json
import re
import time
from text_file_generator import text_file_generator
from clarifai.clarifai_connector import upload_to_clarifai
from google.protobuf.struct_pb2 import Struct

base_url = "https://www.farfetch.com"
REGEX_URL_VIEW = "(view)=\d+"
REGEX_URL_OFFSET = "(page)=\d+"

image_counter = 0
product_counter = 0
page_counter = 0
elapsed_scraping_time = 0.0
elapsed_uploading_time = 0.0
per_url_images = 0


try:
    for page in range(279, 280):
        url = "https://www.farfetch.com/bd/plpslice/listing-api/products-facets?pagetype=Shopping&gender=Women&pricetype=FullPrice&c-category=135967&page=0&view=180"
        url = re.sub(REGEX_URL_VIEW, "view=180", url)
        url = re.sub(REGEX_URL_OFFSET, f'page={page}', url)
        per_url_images = 0
        scrap_start = time.time()

        response = requests.get(url)

        while response.status_code != 200:
            response = requests.get(url)
            print(response.status_code)
            print("retrying after 5 sec")
            print(url)
            time.sleep(5)
            print("5 sec done")

        if response.status_code == 200:
            print(response.status_code)
            print(url)

        json_data = json.loads(response.text.encode('utf8'))

        scrap_end = time.time()
        elapsed_scraping_time += scrap_end-scrap_start

        if len(json_data['listingItems']['items']) == 0:
            print("no products")
            break
        else:
            print(len(json_data['listingItems']['items']))

        products_list = []

        for product in json_data['listingItems']['items']:
            images = []
            if product["url"] not in products_list:
                product_counter += 1
                name = product["shortDescription"]
                product_url = base_url+product["url"]
                products_list.append(product_url)
                brand = product["brand"]["name"]
                price = product["priceInfo"]["finalPrice"]

                if "cutOut" in product["images"]:
                    images.append(product["images"]['cutOut'])
                if "model" in product["images"]:
                    images.append(product["images"]['model'])

                input_metadata = Struct()
                image_metadata = {"name": name, "brand": brand, "price": price, "url": product_url}
                input_metadata.update(image_metadata)

                for image in images:
                    image_url = image
                    upload_start = time.time()
                    value = upload_to_clarifai(input_metadata=input_metadata, image_url=image_url,
                                               image_counter=image_counter)
                    upload_end = time.time()
                    elapsed_uploading_time += upload_end - upload_start
                    image_counter = value
                    if page_counter > 0 and image_counter % 5000 == 0:
                        print("another 5000 done to clarifai")

                per_url_images += len(images)

            else:
                print("duplicate found")
                print(product["shortDescription"])
                print(base_url+product["url"])

        page_counter = page
        print(f"uploaded={image_counter}, products_url={len(products_list)} products_total={product_counter} page_counter={page}")


finally:
    elapsed_uploading_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_uploading_time))
    elapsed_scraping_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_scraping_time))
    text = f"uploaded={image_counter}, products={product_counter} page={page_counter} category=Women all Clothing uploading_time={elapsed_uploading_time} scraping_time={elapsed_scraping_time}"
    filename = "farfetch_data_report"
    text_file_generator(filename, text)
    print(text)







