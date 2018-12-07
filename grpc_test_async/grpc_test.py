#!/usr/bin/python3
# grpc_base.py
#
#  grpc test
#
#  Copyright (C) 2018-2018 huangdeng @ chengdu
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  2018.10.21 init


import grpc
import helloworld_pb2_grpc
import helloworld_pb2


class GrpcStub:
    def __init__(self):
        self._stub = helloworld_pb2_grpc.GreeterStub(grpc.insecure_channel("localhost:50051"))

    def run(self):
        response = self._stub.SayHello(helloworld_pb2.HelloRequest(name='huangdeng'))
        print(response)


if __name__ == '__main__':
    p = GrpcStub()
    p.run()
