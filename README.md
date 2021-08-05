## Using gRPC with Python
In this repositorie we can see an example implementing gRPC with Python for generated a service for calculate de sqrt of a number integer.

# installing dependencies
pip install grpcio grpcio-tools

# Creating files from .proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto