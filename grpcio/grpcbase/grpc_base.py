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
from . import dcopintf_pb2
from . import dcopintf_pb2_grpc
from . import errinf_base


def get_one(element):
    STR_TYPE = [10, 9, 18, 19, 20, 21, 11]
    INT_TYPE = [6, 5]
    DWORD_TYPE = [1, 2, 3, 4, 7]
    QWORD_TYPE = [23]
    BOOL_TYPE = [8]
    BUFFER_TYPE = [11]
    DOUBLE_TYPE = [16, 17]

    data_type = element.Type
    if data_type in STR_TYPE:
        return element.strVal
    if data_type in DWORD_TYPE:
        return '%u' % element.dwVal
    if data_type in INT_TYPE:
        return '%d' % element.iVal
    if data_type in QWORD_TYPE:
        return '%u' % element.qwVal
    if data_type in DOUBLE_TYPE:
        return '%f' % element.dbVal
    if data_type in BOOL_TYPE:
        if element.iVal:
            return 'True'
        else:
            return 'False'

    return element.strVal


def fmt_line(lines):
    col_max_wide = dict()
    for line in lines:
        col_index = 0
        for element in line:
            str_len = len(element)
            if col_index not in col_max_wide or col_max_wide[col_index] < (str_len + 6):
                col_max_wide[col_index] = str_len + 6
            col_index += 1

    fmt_lines = []
    for line in lines:
        col_index = 0
        tmp = ''
        for element in line:
            tmp += format(element, '<%d' % col_max_wide[col_index])
            col_index += 1
        fmt_lines.append(tmp)

    return fmt_lines


def connect_no_ssl(target):
    return grpc.insecure_channel(target)


class GrpcStub:
    def __init__(self, target):
        self._stub = dcopintf_pb2_grpc.GrpcRequestStub(connect_no_ssl(target))

    def run(self, command):
        response = self._stub.ProcessRequest(dcopintf_pb2.PbRequest(CmdLine=command))
        return GrpcStub.fmt_rsp(response), response

    def fmt_rsp(response):
        if not response:
            return 'No Response'

        col_count = len(response.Field)
        result = response.Result
        line_count = response.Count
        title = response.Title
        fmt_result = [title]

        if col_count == 1:
            content = GrpcStub.fmt_line(response, line_count)
        else:
            content = GrpcStub.fmt_mult_line(response, line_count)

        for line in content:
            fmt_result.append(line)

        fmt_result.append(errinf_base.get_err_string(result))
        fmt_result.append('##################################')
        return fmt_result

    def fmt_mult_line(response, total_count):
        str_elements = []
        str_lines = []
        for col in response.Field:
            str_elements.append(col)
        str_lines.append(str_elements)
        str_elements = []

        for x in range(0, total_count):
            line = response.Row.pop()
            for element in line.ColVal:
                str_elements.append(get_one(element))
            str_lines.append(str_elements)
            str_elements = []

        return fmt_line(str_lines)

    def fmt_line(response, total_count):
        str_lines = []

        for col in response.Field:
            str_lines.append(col)

        for x in range(0, total_count):
            line = response.Row.pop()
            for element in line.ColVal:
                str_lines.append(get_one(element))
        return str_lines
