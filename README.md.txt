# installing dependencies
pip install grpcio grpcio-tools

# Creating files from .proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto