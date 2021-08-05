import grpc


# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto



# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
number = calculator_pb2.Number(value=144)

# make the call
response = stub.SquareRoot(number)

# et voila
print(response.value)