from concurrent import futures

import os
import grpc

import test_pb2
import test_pb2_grpc

class ImageBuilderServicer(test_pb2_grpc.ImageBuilderServicer):
    def __init__(self):
        pass

    def BuildImage(self, request, context):
        print("Creating image")
        # get information from request
        print("Request details:", request)
        # build the image using packer build
        os.system('echo Run build step')
        return test_pb2.FinishedImage(image_name = request.node_name)

    def DeployInfra(self, request, context):
        print("Deploying the infrastructure")

    def CreateKeyPair(self, request, context):
        print("Generating your key pair")
        # specify a file path and key name


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_ImageBuilderServicer_to_server( ImageBuilderServicer(), server)
    server.add_insecure_port('[::]:3001')
    server.start()
    print('Listening on port 3001')
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
