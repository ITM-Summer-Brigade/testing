from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import grpc, sys
sys.path.insert(0, '../grpc-server')
import test_pb2
import test_pb2_grpc



app = FastAPI()

origins = ['http://localhost:3000','http://localhost:3001', 'http://localhost:3005']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*'],
    allow_headers=['*']
)

class Image:
    image_name: str
    def __init__(self, node_name):
        self.image_name = node_name


    def build_image(self, stub, name):
        image = stub.BuildImage(test_pb2.ImageDetails(node_name=name))
        if not image.image_name:
            print("Image details are missing")
            return
        
        print(f'Image name called ${image.image_name}')
        return image

    def run_build_image(self,name):
        # with statement makes this smoother
        channel = grpc.insecure_channel('localhost:3001')
        stub = test_pb2_grpc.ImageBuilderStub(channel)
        try:
            self.build_image(stub, name)
        finally:
            channel.close()

@app.get('/')
async def main():
    return {"message": "Hello World"}

@app.post('/images/create')
async def create(request: Request):
    body = await request.json()
    image = Image(node_name=body['data']['image_name'])
    image.run_build_image(image.image_name)
    return image
