import os
import json
import urllib.request
import pandas as pd
from google.protobuf.struct_pb2 import Struct


from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_pb2, status_code_pb2


from api_data.nord_men_clothing import data

# Construct one of the channels you want to use
channel = ClarifaiChannel.get_json_channel()
# channel = ClarifaiChannel.get_insecure_grpc_channel()

# Note: You can also use a secure (encrypted) ClarifaiChannel.get_grpc_channel() however
# it is currently not possible to use it with the latest gRPC version

stub = service_pb2_grpc.V2Stub(channel)

# This will be used by every Clarifai endpoint call.
metadata = (('authorization', 'Key 89f9bd543e4a4bd0b23ef96c466c05cd'),)


base_url = "https://www.nordstrom.com"
to_py = json.loads(data)
i = 0
for product_id in to_py['productsById']:
    print(product_id)
    if i>30:
        break

    for key in product_id:

        if i > 30:
            break
        images =[]
        name = product_id[key]['name']
        brand = product_id[key]['brandName']
        colors = product_id[key]['colorCount']
        url = base_url + product_id[key]['productPageUrl']
        price = product_id[key]["pricesById"]["original"]["minItemPrice"]
        input_metadata = Struct()
        image_metadata = {"name": name, "brand": brand, "price": price, "url": url}
        input_metadata.update(image_metadata)

        for media_id in product_id[key]['mediaById']:

            if i > 30:
                break
            image_url = product_id[key]['mediaById'][media_id]['src']
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





