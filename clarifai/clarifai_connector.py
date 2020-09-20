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
metadata = (('authorization', 'Key 8dc2482f37264e309452e3725c1b474c'),) #my model
# metadata = (('authorization', 'Key 184ff6289859470eacf6da31a9ccb7fc'),)


def upload_to_clarifai(input_metadata, image_url, image_counter):
    post_inputs_response = stub.PostInputs(
        service_pb2.PostInputsRequest(
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(
                            url=image_url,
                            allow_duplicate_url=False
                        ),
                        metadata=input_metadata
                    )
                )
            ]
        ),
        metadata=metadata
    )

    if post_inputs_response.status.code != status_code_pb2.SUCCESS:
        print("Post inputs failed, status: " + post_inputs_response.status.description)
        return image_counter
    else:
        return image_counter+1
