import requests
import json
import re
import time
from text_file_generator import text_file_generator
from clarifai.clarifai_connector import upload_to_clarifai
base_url = "https://www.nordstrom.com"

REGEX_URL_COUNT = "(top)=\d+"
REGEX_URL_OFFSET = "(offset)=\d+"

image_counter = 0
product_counter = 0
page_counter = 0

elapsed_scraping_time = 0.0
elapsed_uploading_time = 0.0

try:
    for page in range(1, 500):
        scrap_start = time.time()

        url = "https://www.nordstrom.com/api/browse/browse/women/clothing?top=72&breadcrumb=Home%2FWomen%2FClothing&origin=topnav&offset=0"
        url = re.sub(REGEX_URL_OFFSET, f'page={page}', url)
        page_counter = page

        payload = "<file contents here>"
        headers = {
            'Host'               : 'www.nordstrom.com',
            'User-Agent'         : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
            'Accept'             : '*/*',
            'Accept-Language'    : 'en-US,en;q=0.5',
            'Accept-Encoding'    : 'gzip, deflate, br',
            'Referer'            : 'https://www.nordstrom.com/browse/women/accessories?breadcrumb=Home%2FWomen%2FAccessories&origin=topnav&offset=3&page=2',
            'Content-Type'       : 'application/json',
            'Country-Code'       : 'BD',
            'Currency-Code'      : 'USD',
            'ExperimentId'       : 'c4619127-f70e-4200-afef-af7d0775d371',
            'IsUserEventQualified': 'false',
            'NordApiVersion'     : '1.0',
            'UserAuthentication' : 'Anonymous',
            'UserId'             : 'e24194ce71c140b7908c13fb040c5932',
            'UserQualificationType': '-1',
            'IncludeContent'     : 'false',
            'IsMobile'           : 'false',
            'nord-request-id'    : 'a674b284-3ecf-45ef-bfd6-eafb971473c4',
            'Nord-SearchAPI-Version': '1',
            'CustomerAuthState'  : 'anonymous',
            'CardMember'         : 'Non-CardMember',
            'VisitorStatus'      : 'New Customer',
            'LoyaltyLevel'       : 'non-member',
            'nord-country-code'  : 'US',
            'tracecontext'       : 'cd561286-93c1-4d9a-8c1b-ef44bd065376',
            'identified-bot'     : 'False',
            'experiments'        : '{"experiments":[{"n":"437kf","ns":"ns-cvnr5","v":"pathB"},{"n":"6uj8l","ns":"ns-2sxt3","v":"Default"},{"n":"FMRecs","ns":"ns-nml15","v":"SB_3_FM"},{"n":"LxRedSalePrc","ns":"ns-3d3au","v":"RedPriceBelow"},{"n":"RedSaleItems","ns":"ns-ronul","v":"Red"},{"n":"SBNNAP","ns":"ns-445hk","v":"NAP"},{"n":"Search2","ns":"ns-4gtrg","v":"Search2"},{"n":"gy7dk","ns":"ns-2cqtx","v":"prioritize"},{"n":"lessspace","ns":"ns-590du","v":"Default"},{"n":"nb2k5","ns":"ns-a97b4","v":"ToggleColor"},{"n":"qiddh","ns":"ns-iyx2g","v":"altimagehover"},{"n":"rerank-4v2","ns":"ns-g4s40","v":"PDP_1_NN_RERANK"},{"n":"retry-card","ns":"ns-2016v","v":"retry-card"},{"n":"w8zt4","ns":"ns-p5bds","v":"voting"},{"n":"x4uou","ns":"ns-euv55","v":"Default"},{"n":"zkiau","ns":"ns-q0ogb","v":"NoAuto"},{"n":"ob0gi","ns":"ns-jflxa","v":"phase3"}],"user_id":"c4619127-f70e-4200-afef-af7d0775d371"}',
            'X-y8S6k3DB-f'       : 'A10VoJh0AQAALrFCz5OMbHyqjUgbXaWYw7yJWl7o6ou4pRwB4fJYh0xnVBwIARt7_fKcuBShwH8AAEB3AAAAAA==',
            'X-y8S6k3DB-b'       : 'x9wria',
            'X-y8S6k3DB-c'       : 'AEAVnJh0AQAAPbuKDkqSWTx4zOPZLtgcGexl7VAYlNmFYQSeuahadLzPvIh0',
            'X-y8S6k3DB-d'       : 'AAaihIjBDKGNgUGASZAQhISy1WKoWnS8z7yIdPG1c-1JbjfsAFCzLTSdgqOsRtUuRgVzaT0',
            'X-y8S6k3DB-z'       : 'q',
            'X-y8S6k3DB-a'       : 'BTQu2dC=JuL8ad3RFgdM=RSE9mGA13Kbyzd3j1PT-Ur5xrJ=e2SXFuRxI9Vq65dcC-qRla-f0yFKSPF9AI_Gd6nFhRNjWm2t2XnqGusBklGQaQRBe42q_o1u76I5JjbmgxBElv_5Pc2jVVF-tkOlUSg26sUmArwLRcb-INaHFtz2-LcqYK3bxpwh0VALbo8zl3uK0XVt25pIJKRnfT_QAarDCnF6hUDuxK=68CHas0u4TMlkA2stT=6Hs-3jvRhv0R6pRS-Fhntm3x09PQ9R=GdefOIqXgavZqcdZ-Fsg2DFGLF3Hrls12vdKWlVY8VcVdj7eoXQDhFugF3VWP3xQrKQmetOgLx3rDrM8RQErAlZjkdq7S1PWe3hr10rcPhBORC4XcV01VdAkAotRr9QYQt3y=D4oAbdQmTN0_byADwmoHEjW1XMOtZg2Yk-H75Mhag8bQ5RFHXtEDwcnHdSUMpJAoQXxwMpPaT7rGzSmHfrfMNXlkOpDqV1Ks7ugC7VfHyaMedJ9AZTRXqpEkemFWQ5ebDQZt4bMHzuOKe1gGGw8t3cxKFpJX5KK0v_M-xFP5IlCSTdpgGKpcr-apAvVENPF49OoVkG2XWYEHQ-bQX3KtUYV-w7DNZ1puQv-I4IIP51GQTOwC3_Y7zpnlRTqBXFDlOMU3UCIP=zT-su7LnNEMLMxAPL=8ZMjHzlfOWeyNrQ9ISDfHHwF0Ck20S5Y0kyseMvCph5gcyzXr3QATGO580myyFxecudyN3kpgWsqHUv4qP9Psq4RIgTZPdSML0g867M9mGZDzx5kl=huTSyswU_vRBd6g0XVVQ7sDy8JOstuJe=wtd3LvQkMsmMZpJYG2GLLMMwOuyAu6Bv70Tqo93VxeJyyUrRUa=tpxOKC2jOEAMw-uxkEWuLnmrQZdbYzeQA4mRX9qG26spZxBQD7UWAbuAPKbcRXfn83=kHSvKYDJVP_aqeQr18J=UoPpNcQBwcK=WhST5BEESE5DhXPyxttyqn3nRT1Z1vxvSTSLPjn0LOukTbuShHLSLOSo7SBcIFSXI5fbJHJuOEsP-l8Iwo3RYwn=BJwdmjMq3jyUcZm3=rnnUVQrGjA8Xa437QZ-1kNG7jn7YHnowgmSPvXlkMppnMBQQUJM4z4A4oo5DXnFm3ALr=tyjFJtTVEDVwXjR4H0bTEVmH=yPD94nG0mLHlh0lc0mz1efKqz9qgKVuDej2VlDCB9BmEED6r1I7FxW2M_XuDP8CeYwpMowbM4e1Fs4=8TF2r-yb6hCUOTKSc38G8LyPzRVJ6vhmB-Gm9otprG__cE1=w8uD2FZ2wTs_6WcwEnn=V7BKESxbOmAu7P-UguVPWaRKaNtStbxbg_Rsyo4g5_hMxX3RwEm1ytROwcjXYUlGmn7=TaSDVMCXPdfEl2njXVkeWNZ4klsPxs0_4xzGhBK2c4lzCnCU90c3b9ydq8ggZO-E9tTS20HvKad4M4JGPIaBoABAIYjH4bc0NtVV7fdvP_8g6WIVoEbvhDkWqtOqXCXuktpTfjV-BhIjOnRv6myYsLEDb9nnclGh5wNbFvPxlYzA-NV2lHU2SBAV5jbV4WWxfVSrwL463NtQPKa-=fhKdL4CCauDEaPgOtkEAGzGOgJFMPEx7NOgotJbWqdwP_OxHG-rndY-e8pOytALgsR02OeMsNluGPboS_p29KxocXI52TDSFrq6S3Q206ZVjYq7AAPPOF8uc0OJE0MEIpjjOFXxEDmq75_Ma1mtDVoVDK-heGllxlA_mN9GMnvXKVgIOQ2F14fcxfS=UwddZ=lsPdjNE9VMtuQvkN9lfubVSwB=M-HbB4Xf_w2cdNH7zW7RG9ryIJY28tXM2H6h=QyPp27PBoatGbhPX6qNOLK9Y2Z9VhcEhnD-4TX57AJCDOXqOheX1HQUUYNFjGuFP1rKyyHcdtaaOZVMQsdWf1SymLreMxNFClgBYqH=n2FMakmC0dZjjGbrmaJUy_yh7W7k-0NqZeluOgL_0ECExsz8Nrulez8y0r8vWrSR=qbBSMJSF31MP3gJbCV_jGmzmGgJvpHfH4D=XF4GZIx8b4gThvEqP95hn=YlwuusYQdvEWZn=sw2tZxMdv6TT7BT6T_Tl3rZ=9OSHWxnkf2Ydbrf8mrYIpsnEywlfzj3dHcyNq6GQ8Ut5gZMEzg69xaZtcVEHm7xolGl4Y6qtwHO5ar_WAwEyplA8Nh9fxqho=CxRQggQKydObTB4_nupAcBetvrMkuWAPhoerx8oPPN9Uz9B20QhQdHsCaR1aN6B=RCeCVLYnl9KY5SwslOZ_kjL=0LuIbhlG=tEEOHc=FKsUybQY3vAz-ahyxhfSEygXkQ_1fsEYdffXyTSfAOaToR94hRMISNA6fPLJnJOT8-VooXNMn=AZ_eaNWKnmeLm6_Mn1M6ySvYHc6d1eUQUYPLkAvjFDFbtZ-jlwJ1brhq-9pfs28-ORgUjpRWs4AQc1md=vn_PgZCyHowwng5evg6dkTHENrUaCkynNQ4TEfl77UGfGBQ-BOzRerCpWZrJWr-P5SyuaFBsBVvENFhds5YDNNgfquaQ1MPmTWfv=6fCuO3Kqk_c_RHXdMoZnZBzVSBatV30DvYmGl=Wt-DnxK8N0tnL8I8GBGnQ3mmdLfQCqbd-=y6y3N-T534RlSt5ypFXpUk3IZkcF30X7IdERqzPnO86IzesS7-9=s8-wby8jQWSzJTRCJFEDLcKwYg5OJInpSRA1pLzT=tVWd-qIFvypBWq1hozke5Ahq4HpvBx-j-49K3vAGagCX64cv3a-6OKx_M=LTpPWMUn9efBEDEnEYDtb_9sokDh-Ny-ofYmBqjRDXlU0YgdoU1r04PRU7kjqpN_SoIYHj2Qw=CdhhJNbPl51R6AH0mkZha4p-0pf11Nq431DSZ6_C=GRTcDdtqq0uJ9Bbq1kUF3h-3Abgbt3trZtxYFyVKlAwECykmvVNmkfGI=3mrDt3OYbusphJ2SHJlhyYUblKvldt5aFP50WA9A_8yKFENCsRSA6aXeE7xJTpzo0jvPrQym9kyJaawxq5bhZbSj6ywx5cLfIqcEqq2KGkNskKC8G8pdT3tw2tTMfHa0ZX0mceTbDYc3s3JoxPpvWHhCTYE_0==V9v2gyUz6Lwc=UIeM_ul-_mP2bGyvcC-Z41SdcW9tuAlljZaCWsHjdzPxMQGIMzAAXIFvAeQz6YH70ANAHZtxCEUQ7DIQ9-DvZTsB1q426q8AuchH8TAhRPU4PahDubfyemR-Pv4UqjPf2=806GVS=Eyg1AJrV5DyzKm6MflmuvdV4BXe5Twpc2m6ahRoD-_rlGSPLbfeFEa6quEQ5ULzJgoJOsQelY2bMe7uQ-VSj0=K2p58VhDuoAWzv5W1VXapC_usktLJcCoyssTHeZRQYpvc7A0MI8LPqp7EoMrNaRyIT8XCgOeHwVbUlhqahLcR55N07QDX9ayTm_lhfDvdeJyB9QuVIUl_z4NZLb2SrqlvJYqvbaglgxhedsVveIt1IoqDNIdy1dDo2J_TpcXC1zGgMUsdBl0=ydsmGplbze4Q7QsP=e=9VpRDkd_l5o9le=O_O2NwS0uEetldf-2m5Jy6o8CI10sgcDJ-IlG0A2W-P=E3XheAH=7dotRc12yMV3hjDXI5cXCD7yNjIb5eHCYcTbcSEXZ4y=YbRwUDoUSdWCHTAnzQ=msymCuqRT476g7Pp4kZUW',
            'DNT'                : '1',
            'Connection'         : 'keep-alive',
            'Cookie'             : 'Ad34bsY56=AIknnJh0AQAAR4VOCsIol2tw3NmhD_JJFiUp-pxNMG8g2Zz6v8kjDT2GWZMo|1|1|0f0b4f0d67f37f1cb6bd1de9ab18322a3d46362b; shopping-bag-migration=shopperId=e24194ce71c140b7908c13fb040c5932&isMigrated=true; rfx-forex-rate=currencyCode=BDT&exchangeRate=91.439&quoteId=70713475; GeoLocationZipCode=undefined; internationalshippref=preferredcountry=BD&preferredcurrency=BDT&preferredcountryname=Bangladesh; no-track=ccpa=false; nordstrom=bagcount=0&firstname=&ispinned=False&isSocial=False&shopperattr=||0|False|-1&shopperid=e24194ce71c140b7908c13fb040c5932&USERNAME=; nui=firstVisit=2020-09-16T20%3A30%3A05.857Z&geoLocation=&isModified=false&lme=false; session=FILTERSTATE=&RESULTBACK=&RETURNURL=http%3A%2F%2Fshop.nordstrom.com&SEARCHRETURNURL=http%3A%2F%2Fshop.nordstrom.com&FLSEmployeeNumber=&FLSRegisterNumber=&FLSStoreNumber=&FLSPOSType=&gctoken=&CookieDomain=&IsStoreModeActive=0; shoppertoken=shopperToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlMjQxOTRjZTcxYzE0MGI3OTA4YzEzZmIwNDBjNTkzMiIsImF1ZCI6Imd1ZXN0IiwiaXNzIjoibm9yZHN0cm9tLWd1ZXN0LWF1dGgiLCJleHAiOjE5MTU4MjEwMDUsInJlZnJlc2giOjE2MDAzMDI2MDUsImp0aSI6ImNlNGI5Y2JmLTEwNzgtNDU4NC04MDljLTdlZWZhZDNjYzMxOCIsImlhdCI6MTYwMDI4ODIwNX0.BQYFf7vdkhiYGY6ANXqwRGl6W_BB-tli5pNoG57wIde7bfNWqESnhdQB1HK_s2M_hW0P3Gg33KCjAEHRiVp6nz1LNcTXe8kArSZXPwl9ddvVNknRVpdxuRvo1_Sl1MWhmgUwHicsf5cAv6_q_5XPYnHFxQYT8nCV9tsDJahFMMzIz6j3myohmI47yUSu-LjnZzf_ULPtNfWV_XdiYi60ac4NuE_1LA8H7gx0mCYADL8Qab-O7mygUbDTS7qtr4O6UUyKIGDyr5cQBcpUGTdpBbx2Iv1hugbDa30tMNyI0B_J9ANlLagCi9hXFgua3x1E84S8o-yyGik2Snw5TwNXag; usersession=CookieDomain=nordstrom.com&SessionId=cd81a0bf-cc0c-47cc-a1ee-3c8e9d07f50f; experiments=ExperimentId=c4619127-f70e-4200-afef-af7d0775d371; Bd34bsY56=AMEjoJh0AQAAygkUXkvedL47DALf8Js7Xvfut9GOCD_frxC30QDx26j3d0-Q; forterToken=881bb91e0e364a92a7223a761be5e1cd_1600288461036__UDF43_6; _gcl_au=1.1.1160322109.1600288207; wlcme=true; rkglsid=h-3b314b99e8add008fe10100174989c30_t-1600288463; _ga=GA1.1.1856209750.1600288207; _ga_XWLT9WQ1YB=GS1.1.1600288206.1.1.1600288462.0; storemode=postalCode=&selectedStoreIds=&storesById=&localMarketId=&localMarketsById=; storeprefs=|100|||2020-09-16T20:34:23.410Z; ftr_ncd=6; _4c_mc_=2bb06f00-868f-41d6-a748-49339c04cf18; buynow=isRegistered=false&isQualified=false; _pin_unauth=dWlkPVkySmxOR1ZtT1dZdE5XTXlNUzAwWkdNMkxUa3lPRE10WkRnMk9UUTJOREUzTVdZMiZycD1abUZzYzJV; minibag=MiniBagHash=1600288463979; _sp_id.c229=c4619127-f70e-4200-afef-af7d0775d371.1600288208723.1.1600288208723.1600288208723.0a7ba402-3e11-45b1-8bd4-a05fe85baa00; _sp_ses.c229=*; Ad34bsY56_dc=%7B%22c%22%3A%20%22ZDlwQUhyRlVoNU1ma0FtdQ%3D%3DZEh0QEhLqx3c4be0Z_NnUUx2TL6IVH-vM18mRLpO2m0JpyHZu_R4V4lPCCKltqyOR80-8mSRN4CyNLCXNMOqQuLsjqJmWQ%3D%3D%22%2C%20%22dc%22%3A%200%2C%20%22mf%22%3A%200%7D; _uetsid=6cbaa24b4796f3c6d3cba6d2d0e451eb; _uetvid=a97ef5ba0129ba3defc9e56abcd88a1c; Ad34bsY56=AM45voB0AQAAPj149mkQI9rUQ3iQ5_JOz5d0i24vpOHlWqgvm5a5tv_UYKsX|1|0|869c24e54f9ca5755f4901dc50c7fba3d5fc30a9; experiments=ExperimentId=a44fc296-4729-484a-a903-15ec1306a09c; shopping-bag-migration=shopperId=e24194ce71c140b7908c13fb040c5932&isMigrated=true; Bd34bsY56=AHdS1ph0AQAA6DmcvD3A7aD9y42uvfZN0sUmzHFXiSY3rBI9L_QoO9ypi_ls',
            'TE'                 : 'Trailers'
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(response.status_code)
            print(url)
            break
        else:
            print(response.status_code)
            print(url)
        json_data = json.loads(response.text.encode('utf8'))

        scrap_end = time.time()
        elapsed_scraping_time += scrap_end-scrap_start

        image_counter = 0
        product_counter = 0
        if len(json_data['productsById']) == 0:
            print("no products")
            break
        for product_id in json_data['productsById']:
            product_counter += 1

            name = json_data['productsById'][product_id]["name"]
            brand = json_data['productsById'][product_id]['brandName']
            colors = ', '.join(json_data['productsById'][product_id]['colorIds'])
            url = base_url + json_data['productsById'][product_id]['productPageUrl']
            price = json_data['productsById'][product_id]["pricesById"]["original"]["minItemPrice"]
            image_metadata = {"name": name, "brand": brand, "price": price, "url": url}
            for media_id in json_data['productsById'][product_id]['mediaById']:
                if json_data['productsById'][product_id]['mediaById'][media_id]['group'] == "main":
                    image_url = json_data['productsById'][product_id]['mediaById'][media_id]['src']
                    upload_start = time.time()
                    value = upload_to_clarifai(input_metadata=image_metadata, image_url=image_url, image_counter=image_counter)
                    upload_end = time.time()
                    elapsed_uploading_time += upload_end-upload_start
                    image_counter = value
                    if image_counter%1000==0:
                        print()
                        time.sleep(60)

finally:
    elapsed_uploading_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_uploading_time))
    elapsed_scraping_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_scraping_time))
    text = f"uploaded={image_counter}, products={product_counter} page={page_counter} category=Women Clothing uploading_time={elapsed_uploading_time} scraping_time={elapsed_scraping_time}"
    filename = "nordstorm_data_report"
    text_file_generator(filename, text)
    print(text)







