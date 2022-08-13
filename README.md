# Dev Portal
A developer portal that allows users to deploy infrastructure at the click of a button

# GRPC
To update the grpc code, update the protobuf file in the ./protos directory then run 
`$ python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/test.proto`

# Tech Stack
- Python
- gRPC
- React/NextJs
- Typescript
- Terraform