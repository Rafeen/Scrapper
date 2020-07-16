import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import urllib.request

dir_path = os.path.dirname(os.path.realpath(__file__))
baseurl = 'https://www.farfetch.com'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}

cat_link = [['https://www.farfetch.com/bd/shopping/men/clothing-2/items.aspx','Men'],
         ['https://www.farfetch.com/bd/shopping/kids/girls-clothing-4/items.aspx', 'Kids Girls'],
         ['https://www.farfetch.com/bd/shopping/kids/boys-clothing-3/items.aspx', 'Kids Boys'],
         ['https://www.farfetch.com/bd/shopping/women/clothing-1/items.aspx',"Women"]]

for cat in cat_link[1:]:
    r = requests.get(cat[0], headers=headers)
    soup = BeautifulSoup(r.content, "lxml")

    product_list = soup.find_all("li", class_="_c29d78 _d85b45")
    product_links = []

    for item in product_list:
        for link in item.find_all('a', href=True):
            link['href'] = link['href'].replace('bd','us')
            product_links.append(baseurl + link['href'])
    product_links = list(set(product_links))

    products_final_processed_list = []
    not_downloaded = []
    for link in product_links:
        try:
            print(link)
            r = requests.get(link, headers=headers)
            soup = BeautifulSoup(r.content, "lxml")

            brand_name = (soup.find('span', class_='_e87472 _346238 _e4b5ec').text.strip())
            product_name = soup.find('span', class_='_d85b45 _d85b45 _1851d6').text

            full_name = brand_name + " " + product_name
            image_proxy_name = full_name
            full_name = full_name.replace(',', '')
            full_name = full_name.replace("'", '')
            full_name = full_name.replace('"', '')

            try:
                pre_processed_price = soup.find('span', class_='_e806a1 _0f635f').text
            except:
                pre_processed_price = soup.find('span', class_='_89a1d3 _b764f1').text
            price = pre_processed_price.replace('Reg.', '')
            price = price.replace('Orig.', '')

            image_tags = (soup.find_all('img'))
            for i in image_tags:
                if '.jpg' in i['src']:
                    i['src']=i['src'].replace('_80', '_1000')
                    image_name = image_proxy_name + ' ' + i['alt'].strip(f'of {full_name}')

                    my_path = f'\\images\\farfetch\\{cat[1]}'  # use whatever path you like
                    file_path = dir_path + my_path
                    try:
                     urllib.request.urlretrieve(i["src"],
                                               os.path.join(file_path, os.path.basename((image_name + '.jpg'))))
                    except:
                        not_downloaded.append(full_name)


            product = {
                'Name': full_name,
                'Category': cat[1],
                'Price': price,
           }

            products_final_processed_list.append(product)
        except:
            pass

    df = pd.DataFrame(products_final_processed_list, columns=['Name', 'Category', 'Price'])
    df.to_excel(dir_path + f"\\images\\farfetch\\farfetch_{cat[1]}.xlsx", index=False)

    df = pd.DataFrame(not_downloaded, columns=['Name'])
    df.to_excel(dir_path + f"\\images\\farfetch\\farfetch_{cat[1]}_not_downloaded.xlsx", index=False)
    print(f"DONE {cat[1]}")
