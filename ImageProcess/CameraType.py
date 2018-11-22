#!/usr/bin/python3
# -*- coding: utf-8 -*-
# CameraType.py
#
# camera_type covert
#
#  Copyright (C) 2018-2018 huangdeng @ chengdu
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  2018.11.22 init


class CameraTypeConvert:
    def __init__(self):
        self._type = dict()
        self._type['LLD-AL20'] = 'honor 9i'

    def get(self, in_type):
        if in_type in self._type:
            return self._type[in_type]
        else:
            print('Error: Can\'t convert type')
            return 'UnKnown'


g_CameraTypeConverter = CameraTypeConvert()


if __name__ == '__main__':
    print(g_CameraTypeConverter.get('LLD-AL20'))

