#!/usr/bin/python3
# errinfo_base.py
#
#  errinfo test
#
#  Copyright (C) 2018-2018 huangdeng @ chengdu
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  2018.10.21 init

import json
#mport pkgutil

_json_file = 'errinfo.json'


class ErrInfo:
    def __init__(self):
        #json_data = pkgutil.get_data(__package__, _json_file)
        #self._err_json = json.loads(json_data)
        with open(_json_file) as f:
            self._err_json = json.loads(f.read())

    def get(self, err_value):
        json_key = '%d' % err_value
        if json_key in self._err_json:
            return self._err_json[json_key]
        else:
            return '0x%x' % err_value


_g_ErrInfo = ErrInfo()


def get_err_string(value):
    if value == 0:
        return 'Success!'
    else:
        return 'Failed! %s' % _g_ErrInfo.get(value)
