#!/usr/bin/python3
# -*- coding: utf-8 -*-
# checksum.py
#
# checksum
#
#  Copyright (C) 2018-2018 huangdeng @ chengdu
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  2018.10.19 init
import time
import hashlib
import os
import json
import struct

def get_hash():
    return hashlib.sha256()


def get_file_checksum(file):
    with open(file, 'rb') as f:
        real_hash = get_hash()
        real_hash.update(f.read())
        return real_hash.hexdigest()


class Check:
    def __init__(self, root, record):
        self._root = root
        self._skip = len(root)
        self._to_checksum = dict()
        self._build_checksum = dict()
        self._check_file = record

    def load_checksum(self):
        with open(self._check_file) as f:
            self._to_checksum = json.loads(f.read())

    def build_checksum(self):
        for cur_path, dirs, files in os.walk(self._root):
            if cur_path == self._root:
                continue
            if '.resona' in cur_path:
                continue

            for file in files:
                full_path = os.path.join(cur_path, file)
                self._build_checksum[get_file_checksum(full_path)] = full_path[self._skip:]

    def check(self):
        pass

    def build(self):
        self.build_checksum()
        with open(self._check_file, 'w') as f:
            f.write(json.dumps(self._build_checksum, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    start = time.time()
    record = 'D:\weiyun\sync\mycheck.json'
    p = Check('D:\weiyun\calibre', record)
    p.build()
    end = time.time()
    print(end-start)
