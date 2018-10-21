#!/usr/bin/python3
# cli_main.py
#
#  grpc cli maint
#
#  Copyright (C) 2018-2018 huangdeng @ chengdu
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  2018.10.21 init

from grpcio.grpcbase.grpc_base import GrpcStub


class CliMain:
    def __init__(self):
        self._Stub = None
        self._connected = False

    def _print_notice(self):
        if not self._connected:
            print('please input server ip and port to connect')
            print('for help, input: --help')

    def _help(self):
        print('for help, input: --help')
        print('connect, input: conn xxx.xxx.xxx.xxx:xxxx')
        print('send command to server, input:  :youcommand')

    def _command(self, cmd):
        if not self._connected:
            self._print_notice()
            return
        rsp_str, rsp = self._Stub.run(cmd)
        for line in rsp_str:
            print(line)

    def _connect(self, cmd):
        split_cmd = cmd.split()
        if len(split_cmd) == 2:
            self._Stub = GrpcStub(split_cmd[1])
            self._connected = True

    def run(self):
        while True:
            self._print_notice()
            line = input('$')
            if '--help' in line:
                self._help()
            if ':' in line[:2]:
                self._command(line)
            if line[:4] == 'conn':
                self._connect(line)


if __name__ == '__main__':
    p = CliMain()
    p.run()
