from __future__ import print_function

import sys
import grpc
import test_pb2, test_pb2_grpc

def build_image(stub):
    name = sys.argv[1]
    image = stub.BuildImage(test_pb2.ImageDetails(node_name=name))
    if not image.image_name:
        print("Image details are missing")
        return
    
    print(f'Image name called ${image.image_name}')
    return image

def run():
    # with statement makes this smoother
    channel = grpc.insecure_channel('localhost:3001')
    stub = test_pb2_grpc.ImageBuilderStub(channel)
    try:
        build_image(stub)
    finally:
        channel.close()

if __name__ == '__main__':
    run()