# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  user_name=raw_input('What is your name? \n')
  stub = helloworld_pb2_grpc.GreeterStub(channel)
# send server the user name and get the response from sayhello method
  response = stub.SayHello(helloworld_pb2.HelloRequest(name=user_name))
  print("Greeter client received: " + response.message)
# send server the user name and get the response from sayBye method
  response = stub.SayBye(helloworld_pb2.HelloRequest(name=user_name))
  print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
