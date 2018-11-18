#!/usr/bin/python3
# -*- coding: utf-8 -*-
# find_copy_v2.py
#
#  find the equal file in filesystem
#
#  Copyright (C) 2018-2018 huangdeng @ chengdu
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.

__author__ = 'huangdeng'

import os
import hashlib
import time


class Unique:
    def __init__(self):
        self._dict = dict()
        self._equal_files = []
        self._empty_files = []
        self._files = 0

    def _get_key(full_name):
        my_hash = hashlib.sha1()
        with open(full_name, 'rb') as f:
            b = f.read()
            my_hash.update(b)
        return my_hash.hexdigest()

    def _process_equal(self, full_name, key):
        info = [self._dict[key], full_name]
        self._equal_files.append(info)
        if len(self._equal_files) > 50:
            self.output()

    def _process_one(self, fullname):
        if os.path.getsize(fullname) == 0:
            self._empty_files.append(fullname)
            return

        f_key = Unique._get_key(fullname)
        if f_key in self._dict:
            self._process_equal(fullname, f_key)
        else:
            self._dict[f_key] = fullname

    def process(self, root):
        for cur_path, dirs, files in os.walk(root):
            for file in files:
                self._files += 1
                if self._files % 1000 == 0:
                    ptr_str = "\r processed files:%d" % self._files
                    print(ptr_str, end='', flush=True)
                full_name = os.path.join(cur_path, file)
                self._process_one(full_name)

    def output(self):
        print('####### Equal files: #######')
        for one in self._equal_files:
            print('Ori:', one[0])
            print('del "', one[1], '"', sep='')
            print('')
        print('####### Empty files: #######')
        for one in self._empty_files:
            print('Empty file:', one)
        self._empty_files = []
        self._equal_files = []


def test_entry():
    # 需保持的文件目录在前面，前后目录不能有重叠
    to_check_dirs = [r'E:\weiyun\calibre', r'E:\weiyun\toaddbooks']
    p = Unique()
    for one in to_check_dirs:
        p.process(one)
    p.output()


if __name__ == '__main__':
    test_entry()
