import requests
import json
from google.protobuf.struct_pb2 import Struct


from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_pb2, status_code_pb2

# Construct one of the channels you want to use
channel = ClarifaiChannel.get_json_channel()
# channel = ClarifaiChannel.get_insecure_grpc_channel()

# Note: You can also use a secure (encrypted) ClarifaiChannel.get_grpc_channel() however
# it is currently not possible to use it with the latest gRPC version

stub = service_pb2_grpc.V2Stub(channel)

# This will be used by every Clarifai endpoint call.
# metadata = (('authorization', 'Key 39b11cf497514dc891ee6ff03ad93edb'),) #my model
metadata = (('authorization', 'Key 18d1cefe512449579d0178d49fd7a700'),)


base_url = "https://www.nordstrom.com"




men_clothing_api_max_count = '7172'
count = "20"

url = f"https://www.nordstrom.com/api/browse/browse/men/clothing?top={count}&breadcrumb=Home%2FMen%2FClothing&origin=topnav&offset=0"

payload = "<file contents here>"
headers = {
  'Host': 'www.nordstrom.com',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Referer': 'https://www.nordstrom.com/browse/men/clothing?breadcrumb=Home%2FMen%2FClothing&origin=topnav',
  'Content-Type': 'application/json',
  'Country-Code': 'BD',
  'Currency-Code': 'USD',
  'ExperimentId': '3dd33fee-94b9-4290-9501-02e59172964e',
  'IsUserEventQualified': 'false',
  'NordApiVersion': '1.0',
  'UserAuthentication': 'undefined',
  'UserId': 'bab92a9ee1424a339e232945130e93ab',
  'UserQualificationType': '-1',
  'IncludeContent': 'true',
  'IsMobile': 'false',
  'nord-request-id': '854e815a-745e-4df5-9355-8db52a6c40e1',
  'Nord-SearchAPI-Version': '1',
  'CardMember': 'Non-CardMember',
  'VisitorStatus': 'New Customer',
  'LoyaltyLevel': 'non-member',
  'nord-country-code': 'US',
  'tracecontext': 'f46a36ce-6e73-44f5-9e51-10aca70c0fca',
  'identified-bot': 'False',
  'experiments': '{"experiments":[{"n":"437kf","ns":"ns-cvnr5","v":"pathB"},{"n":"6uj8l","ns":"ns-2sxt3","v":"Default"},{"n":"LxRedSalePrc","ns":"ns-3d3au","v":"RedPriceBelow"},{"n":"RedSaleItems","ns":"ns-ronul","v":"Default"},{"n":"SBNNAP","ns":"ns-445hk","v":"NAP"},{"n":"Search2","ns":"ns-4gtrg","v":"Search2"},{"n":"gy7dk","ns":"ns-2cqtx","v":"Default"},{"n":"lessspace","ns":"ns-590du","v":"LessSpace"},{"n":"nb2k5","ns":"ns-a97b4","v":"ToggleColor"},{"n":"qiddh","ns":"ns-iyx2g","v":"altimagehover"},{"n":"rerank-4v2","ns":"ns-g4s40","v":"PDP_1_NN_RERANK"},{"n":"retry-card","ns":"ns-2016v","v":"Default"},{"n":"w8zt4","ns":"ns-p5bds","v":"Default"},{"n":"x4uou","ns":"ns-euv55","v":"Default"},{"n":"ob0gi","ns":"ns-jflxa","v":"phase3"}],"user_id":"3dd33fee-94b9-4290-9501-02e59172964e"}',
  'X-y8S6k3DB-f': 'A9kV0ZN0AQAAHRRirmQ1IBIpbC88_StbZL6tLyh9DoS39OVwxabFOETX0h6CARt7_f6cuNHLwH8AAEB3AAAAAA==',
  'X-y8S6k3DB-b': '-yegzwp',
  'X-y8S6k3DB-c': 'AAAfyJN0AQAAfglxrBTQl8UOmE35DrLlk7uZA1pg6ubVnJGs-xeP07nx4PgT',
  'X-y8S6k3DB-d': 'AAaihIjBDKGNgUGASZAQhISy1WIXj9O58eD4E_G1c-1JbjfsAM_LJtpZi8VjbAiD4RbcVQk',
  'X-y8S6k3DB-z': 'q',
  'X-y8S6k3DB-a': 'Op1xoZLX5njigXskOriPbbk1W9n-MFCyNq5Ual537YWMlwaR6-6eJt3p-veE=CLJBFb1vjLfaCqCe6hahapBML1G-jnQmxJGhEH7g3tIP2eZ_MGl2cE4ggR0QXQN0bJcHOMwFSU-ZmGaqTlHy4r9z4dcENirs28RRjvGOEyTrBJ1GWh1TYg-aRs=5Qk8127R6zBOrf2bmjotqGNHqFa7c3FDsXIi8C-CcOc=-rlNXUEe8S5dZV9yvsOFMYsQ295ZWFIWR8GyraaU0MaT=GeNZFYZobgIQ0gdeIEpqBtsZqYYs52G3D-AH6aK8Bz-_iHcAno4zqwnxGbb29KP-YE4LwnwQGjpolIaspaGKXFv8UG2TL3TBetbDZIXiFnyzkdUKH981y1M7pvlzKqPUsckfgV571m=csJJjD4h7OgI=1z_fh3qoDFYteEstxl2LYpjhsgWXdRgtpav58xzqETrS5htd0QzDdzp79WIQcg32a30_mIpYFdEYhY1oy9_vQo2GHv2gaIaACyDXb73cRJvz2tpk1c5rCvHG5F33=8TjHkqyvnzllU2htDPU2pwnqjscRpMsAfRoDdn0xAL3CQkmxhha7gx9lB90Es2PAbGTKCjrJoXSZf_-NFBaQlxOUUPgjZ9HeYk21wlEJ6P5Zf1E=FQId4PEDrzyU6gBwvZ1cNBMJTVz=y=Qk5KwVIsPWZnYTl6yS4rg7=xG5X=U-YiYYTMSr7PmDIVC1xgmrGyoK79GP-NDtHtrO1da1Bh4XQF1J7xbYsoGORnxArv7oYpoMBefibl-J0Nn-FP2mc6BGaA5GCFj9D9idg=M-rk6BCQ7DpjRBsRec4-2ZJo-tEt5IFWpU3-6WN85vKQSLM=d9KA8DIf=7VZZFw48hxieXrMVSlvtUM=dxglXkl1r6c33Dlqjzet8UbA=tm9yqCzWW7LUyPdczxHlcJR1O7fZJOfEwfYfcVQsO_6EOFQyLGei_BENvIgwww3aZzdynslCI0bTZE_pBYF6ly6AsZYFwJJ-HI93cBKRbxmVxSBKTi9HlX_8WLDTU05Pro8lRN0LYtT-AUDhPsnjJHUa8POsbgv3Q1JLaDgCSk9IjErDljAO57st8J4c0vsxomjNKDKDyt23IePqdeegmbIQFNhX94ywrd4Lcw=jpbWyoCFxFvxxXVACJtNi3bgCv0BZh9l4WaPBeE--C0Nfq70TsXEdoHWW_9E8qrKAM9rbxPwvwOpYTthYefbt-ravIgWztZjq5FBRCR1gO_M0JUmElYTG7Vw-8Cr6wyhEDQsJLPPL7pv64CYyhxHnnx8BgklBj9v7Agqx6cXHW5cj5GBeAtFrn1pfX7FnwaSY0zJDPfa=FNM8-JInmYDIZkXOqK_n9VTlYEVXcr=Uk0fn6eiEy-hFlkly_INyo5gJOtk0ZCAeeq0e3eQxCMg8_9vksy1WxA-KOabR=z_-lgahh08S2PwsjHPc1EYXfdBfILCwJU5bnO7VpkDpaKf53PFdt8eWIaE1yb5AWEGJ4ahIv2o5-kMJ_WRKwOkLgWyjWyS=fFLJs93wo0caUi4cwaGxkYtdBI72BVdDtgNM3lgJK7j_8liknD8NMjbqZ5Hn2vfxkpE6613=5X5K_0s8FBOY=6vzn2eGCmgfIIotTh=TnjY78ip5Qj-tTL=nO17tPHqs76_dlbbbXVsnJT8WE2j5v8wFH8W07RfAs1lv-aX8bXCZ-gFgGpedFNwHNbyYVN5UtKXnOdOoyPgJSbx8StVUmjWLVwP6gfeFm62yOLV7-fY8ZtOKnvtS2P-Teh_6dFlrTL=rTzx=Rm_TN0H1UDvaZVpapkxnCYjRxY0wDWa7xs7aQD93HdTeUvRJ7NZAsX_AGZJjJih9lC2ZDT1soYHjJH1UkzLDCrgdxGbI-yzKtjyN0_yNMHDtO-J2w6iPtCtKD5H71wgJ79J1Gc0TEF39Yhq4lql7UKU5bKG7J_3y-5n=jhJK91Ez4UioH9GcfVEnR-TgsWqrsK=Uya7R8s5Z54aeIFGj4OHKRNA8ZnAzQFHvUR7vQR=pVLzjkxQzYJ169n27PsszeMsAjr6ilf_ze44NQUw0JWnliY6FDWG354JW8zk-wGNgtFGIs5Gzr=T-QTU-IaK0ENHTF=Qd_Na2QMrF6XGe-8mVpZE3yzi7irMBrGOX0l7xsbkPQzWfDK97gqHdmHaLyWPbfjds3pxKG7E9OELovwi2-7GoaRhZEhUw5kgVnQqKb5Ir-MLc=Xf7HMHdQaCUB7HF7RmZL86RPzCqD4RFqFygwDvktpmsGO3WIh=yAqKhzC9H2F27PI=oPropjczE_VyU=Gv0wXYIoKxI4-gwpeN2FYkQnC54trmDX=d7yzcAvFF5Q5lSxMVZzyp2m4WDqvqYQ3GJnN5EfAclxweVLq=jNFhwVV2msLBY3OJj=Str8fkU9pgTQm7ZRIPSHODpOBZFDHLK5SwnvR=g_q6l6EZ85LS7KeEXYBUi2HQdF81b4hr-IqfreTHv-4b4bp0VVOFNtmyaCsz7pJssD44rchETel42eDYdJLLKhWYsTWNkbzn2wlflTM=tixUwc15d-LxgwdaTLLn-vHbesHmKMNXWUfUak37N3WWsr-m6W84h8TIZ0bclMVx034OE=v=bZTlofw=3d8Bgd=BE=YLe4CSHiFm-TzsiqcBCc1XQXUjaUcxxMqNYRYJzM_WBzB4mKoHLJ6C32flxFySpF7pFklWJSBsNmxMCQsMBsv4WrA-UQL1miD4VsC3NNP3l2V7avd8dr4t6_egl3hH9GmfjoktQqKj2AxSNQkk6Laid2CYA8P2_ZEo5-dwMejGwSC55tT1nbB=8L18bkqg70YmUTfYcrGPdVOwT5m=q0UORE2Movm0QvC_WetONSGR_XfDsvAyEmYZHmlJQHHsM8zRNoyZpL81ULhwYbjSImx=rsgvY9Uv0ivm3pS7krtZeZURzq7974T4DwZhLmhMhnOy5YQCY=W1lwoTWBFfK=7iU1niDpgWVm65MC2ajfYRrrD4O_zF0cPmfSjBSfhsi7l1haUwozwLJGGIVNpSje8-4tJVApf--1-9IpcFkrlKTl8zhteeN4SBozwVBURzI8CwjEvySe4Q_6O4N2GyAx249LyR4fJ9dzCkHLAav4R0EXnFgd66BAA6ZXRgQ26jgpzN=rDbLfhAQ9KVQG89z-zo96qy06XtHS4JX1MbUi4QwEPN1eUdIrIG7xgNfMtoQ2to=7tb9VXsqEgwmrrUEUxk91b-L3hhMCQL7pcYxPIOERkYLrDXa6AwVCaz5beHFpMVvjlteNgqkgUwDmidmhNd7N0Tlv-0X5DYRW5XbdAamgRv3BxjMXsEiZ_S7QVdd=A3-Ul3skCr03LGX0jwU3PnlJftx=MMPM=YiojHUC_m=2BsKP2=6Mh5JqeWogUMgq4q8OLKYv4=Lqy8L6nLAHqF3jNmlPPjEmvQA7Slwn4bDPXW1peyd8fSwR_-PyXMOxvmWvb24KBJ4OAT1Ca-zVNxQ7Un_i3r_N884oOvUtmGiDF-2vD_EwL=W0l4XwXkszSOWMocA9LFnSid1DwJihNAH41sGhmG8L1vRxdD1=5RkXamn6r3Tt9H3dXmVn4zB-Mjp2HMK80mibC8cO5PNHLhA8a5x9TTN6kBDJAkrS-VS=yqyB9Yb3mNw5bYdGUJN_sZJ2=oc5UG=N-7vWbTpydUoI=4DiAfGHwV9WCY_yG-N2Ys5itir8M66JJ3Se=CYSldK0fytU',
  'Connection': 'keep-alive',
  'Cookie': 'Ad34bsY56=ADYO0ZN0AQAAIXeVUtyeYNfkbrhna73jVPMgETvubEjK1IdpD5YBG8e4mU9G|1|1|6850f2cafa57b18b3b9fd82228d501c77b316aed; shopping-bag-migration=shopperId=bab92a9ee1424a339e232945130e93ab&isMigrated=true; rfx-forex-rate=currencyCode=BDT&exchangeRate=92.9404&quoteId=70694447; GeoLocationZipCode=undefined; internationalshippref=preferredcountry=BD&preferredcurrency=BDT&preferredcountryname=Bangladesh; no-track=ccpa=false; nordstrom=bagcount=0&firstname=&ispinned=False&isSocial=False&shopperattr=||0|False|-1&shopperid=bab92a9ee1424a339e232945130e93ab&USERNAME=; nui=firstVisit=2020-09-15T22%3A09%3A46.814Z&geoLocation=&isModified=false&lme=false; session=FILTERSTATE=&RESULTBACK=&RETURNURL=http%3A%2F%2Fshop.nordstrom.com&SEARCHRETURNURL=http%3A%2F%2Fshop.nordstrom.com&FLSEmployeeNumber=&FLSRegisterNumber=&FLSStoreNumber=&FLSPOSType=&gctoken=&CookieDomain=&IsStoreModeActive=0; shoppertoken=shopperToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiYWI5MmE5ZWUxNDI0YTMzOWUyMzI5NDUxMzBlOTNhYiIsImF1ZCI6Imd1ZXN0IiwiaXNzIjoibm9yZHN0cm9tLWd1ZXN0LWF1dGgiLCJleHAiOjE5MTU3NDA1ODYsInJlZnJlc2giOjE2MDAyMjIxODYsImp0aSI6ImY3YTliMDQzLTNjMDktNDI5OC05YmQxLTVmNjUxNWY0MzU2OSIsImlhdCI6MTYwMDIwNzc4Nn0.bvwE_RX5DyuMOvzM-Xj60Ed65s0NcudLJMmP-S5xLMUqnb5O9tdpXsMXxXgJ_Pj1XiyhZBumuUGut1KeBKqwYEqgPsIcltPeoAT4g1-lm-kQpTHwSsU0gx-BEWUYIdri-1LQ0Gh4YXaFMhX0PyW8hiuXY83Bbj59hAZRTIdruhtsN69M2AkbvItMFAm2SMNmhjl0AzJxr9bnLhzMHc_Q3Gq3MyFbaQgql9yLB6BRt4SKKZw1_n5R3NZO2AeirJLfAjS1-Hg4W7lotiQwGN_BZsSs8N6SjTmy-R9UnMpStsz6qKppOvRU0FjJr_edFrGjIVlzopIXKSQXf-SQn-4Ygg; usersession=CookieDomain=nordstrom.com&SessionId=29467114-170f-41e6-9eb2-2b2117d3ef21; experiments=ExperimentId=3dd33fee-94b9-4290-9501-02e59172964e; Bd34bsY56=APUw0ZN0AQAAwqWNhjtCZygCH3psSvv_p0octEczG_v4vSJoOQh8SIknDsZe; forterToken=aa3a880099214607a85dae4d58653dfa_1600207786558__UDF43_6; wlcme=true; client=viewport=4_LARGE; storemode=postalCode=&selectedStoreIds=&storesById=&localMarketId=&localMarketsById=; storeprefs=|100|||2020-09-15T22:09:48.318Z; _gcl_au=1.1.1283083124.1600207788; _ga=GA1.2.1206191074.1600207789; _ga_XWLT9WQ1YB=GS1.1.1600207788.1.1.1600207788.0; ftr_ncd=6; rkglsid=h-999ae3aa9e8add027fe1010017493d11_t-1600207789; _gid=GA1.2.1866901018.1600207793; _gat_UA-107105548-1=1; buynow=isRegistered=true&isQualified=false; minibag=MiniBagHash=1600207793516; _4c_mc_=e7d6472d-fe0a-4b55-bd1f-b9c2e7f59cf2; Ad34bsY56_dc=%7B%22c%22%3A%20%22b054cWczUnVTQVJVUHFNWg%3D%3D9u6brAw5E8uYmgo7pByWZgXHHyo_0mCBLCn5UTtQhdLu1BPP-NxCPIxOhLANrU35yYhnA1CGFjjmrn51WeZEAxO6iwzDHw%3D%3D%22%2C%20%22dc%22%3A%200%2C%20%22mf%22%3A%200%7D; _sp_id.c229=3dd33fee-94b9-4290-9501-02e59172964e.1600207791666.1.1600207791666.1600207791666.afb25597-4e99-4c7e-8159-045594b6b051; _sp_ses.c229=*; _pin_unauth=dWlkPVlXTm1NbVV6WVRNdE1XRTNPQzAwT1RZMkxXRXdZVEl0Tm1JM1pERmlZelUyTnpJdyZycD1abUZzYzJV; _fbp=fb.1.1600207797613.1133049266; _uetsid=f7678404e549d06c44ac91b10a3999a0; _uetvid=451874f55640b4bcbc0f4e2cd4457185; Ad34bsY56=AM45voB0AQAAPj149mkQI9rUQ3iQ5_JOz5d0i24vpOHlWqgvm5a5tv_UYKsX|1|0|869c24e54f9ca5755f4901dc50c7fba3d5fc30a9; experiments=ExperimentId=a44fc296-4729-484a-a903-15ec1306a09c; Bd34bsY56=AJvl0pN0AQAAxSsjIupRnZdm3AtmKgO4S79F5t_2JDbR2iTRVdsmjDvP3Be-; shopping-bag-migration=shopperId=bab92a9ee1424a339e232945130e93ab&isMigrated=true',
  'TE': 'Trailers'
}

response = requests.get(url, headers=headers)
json_data = json.loads(response.text.encode('utf8'))

image_counter = 0
product_counter = 0
for product_id in json_data['productsById']:
    product_counter += 1

    name = json_data['productsById'][product_id]["name"]
    brand = json_data['productsById'][product_id]['brandName']
    colors = json_data['productsById'][product_id]['colorCount']
    url = base_url + json_data['productsById'][product_id]['productPageUrl']
    price = json_data['productsById'][product_id]["pricesById"]["original"]["minItemPrice"]
    input_metadata = Struct()
    image_metadata = {"name": name, "brand": brand, "price": price, "url": url}
    input_metadata.update(image_metadata)
    for media_id in json_data['productsById'][product_id]['mediaById']:
        image_url = json_data['productsById'][product_id]['mediaById'][media_id]['src']
        post_inputs_response = stub.PostInputs(
            service_pb2.PostInputsRequest(
                inputs=[
                    resources_pb2.Input(
                        data=resources_pb2.Data(
                            image=resources_pb2.Image(
                                url=image_url,
                                allow_duplicate_url=True
                            ),
                            metadata=input_metadata
                        )
                    )
                ]
            ),
            metadata=metadata
        )

        if post_inputs_response.status.code != status_code_pb2.SUCCESS:
            raise Exception("Post inputs failed, status: " + post_inputs_response.status.description)
        else:
            image_counter += 1
            print(image_counter)


print(f"uploaded {image_counter} images for {product_counter} products")


