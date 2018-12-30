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
        self._type['LLD-AL20'] = 'honor9i'
        self._type['NEX-3N'] = 'sony'
        self._type['NEM-AL10'] = 'honor5ch'
        self._type['E15i'] = 'sony_e15i'
        self._type['Canon PowerShot A720 IS'] = 'canon'
        self._type['INE-AL00'] = 'nova3i'
        self._type['GEM-703L'] = 'honor_x2'
        # self._type['NIKON D90'] = 'nikon'
        self._type['HM1S'] = 'mi1s'
        # elf._type['QCAM-AA'] = ''
        self._type['U8818'] = 'G300'
        self._type['H2A'] = 'mi2a'
        self._type['m1 note'] = 'note'
        self._type['HM 1S'] = 'mi1s'
        self._type['NEM-TL00H'] = 'honor5c'
        # self._type['	iPhone 6s'] = ''
        # self._type['Canon EOS 350D DIGITAL'] = ''

    def get(self, in_type):
        if in_type in self._type:
            return self._type[in_type]
        else:
            print('Error: Can\'t convert type')
            return 'UnKnown'


g_CameraTypeConverter = CameraTypeConvert()


if __name__ == '__main__':
    print(g_CameraTypeConverter.get('LLD-AL20'))

