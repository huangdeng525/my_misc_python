#!/usr/bin/python3
# cmp_disk.py
# 
#  compare two directory's files and ignore directory's structure
# 
#  Copyright (C) 2018-2018 huangdeng @ chengdu
# 
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  2018.3.13 optimization speed

import os
import hashlib
import time


def get_hash_key(file):
    my_hash = hashlib.sha1()
    with open(file, 'rb') as f:
        b = f.read()
        my_hash.update(b)
    return my_hash.hexdigest()


def get_file_size(file):
    """
        other get file size function
        #f = open(file, 'rb')
        #f.seek(0, 2)
        #return f.tell()

        #return os.stat(file).st_size
    """
    return os.path.getsize(file)


def get_file_key(file):
    key = get_file_size(file)
    if key == 0:
        return 0
    # if file size over 8M, then use file size as key
    # 20180314 suit for photo raw file: all file has one size
    if key < (32 * 1024 * 1024):
        key = get_hash_key(file)
    else:
        key = str(key)

    return key


def compare_with_binary(left, right):
    if get_file_size(left) != get_file_size(right):
        return False

    with open(left, 'rb') as l_f:
        with open(right, 'rb') as r_f:
            while True:
                l_v = l_f.read(4096)
                r_v = r_f.read(4096)
                if l_v != r_v:
                    return False
                if not l_v and not r_v:
                    break
    return True


def process_equal_file(new_f, old_f, file_key):
    if compare_with_binary(new_f, old_f):
        pass
    else:



class CmpDirectory:
    def __init__(self, is_del, ref_dir, to_check_dir):
        self._is_del = is_del
        self._ref_dir = ref_dir
        self._to_check_dir = to_check_dir

    def run(self):
        build_ref_dict()
        if