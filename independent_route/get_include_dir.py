#!/usr/bin/python3
# -*- coding: utf-8 -*-
# get_include_dir.py
#
# build my include dictionary
#
#  Copyright (C) 2018-2018 huangdeng @ chengdu
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  2018.8.30 init
__author__ = 'huangdeng'

import os


def get_include_dir(root, replace_with):
    for cur_path, dirs, files in os.walk(root):
        for file in files:
            if '.h' in file:
                include_path = cur_path.replace(root, replace_with)
                print(include_path)
                break


if __name__ == '__main__':
        get_include_dir(r'E:\github\dcop', r'-I ..\..\..')