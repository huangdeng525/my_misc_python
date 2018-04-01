#!/usr/bin/python3
# -*- coding: utf-8 -*-
# find_copy.py
# 
#  find the equal file in filesystem
# 
#  Copyright (C) 2018-2018 huangdeng @ chengdu
# 
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  2018.3.13 optimization speed
#  2018.3.14 suit for photo raw file: all file has one size, reset low length to 32M
#  2018.3.15 for size equal file, execute binary compare
#  2018.3.16 exclude file of size 0

__author__ = 'huangdeng'

import os
import hashlib
import time

_total_file_num = 0
_equal_file_num = 0
_debug_flag_ = False
_out_str = []


def my_output(level, prt_str):
    global _out_str
    if level == 0:
        _out_str.append(prt_str)
        #print(prt_str)
    if level == 1 and _debug_flag_:
        _out_str.append(prt_str)


def print_my_output():
    global _out_str
    for info in _out_str:
        print(info)


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
    before_time = time.time()

    key = get_file_size(file)
    if key == 0:
        return 0
    # if file size over 8M, then use file size as key
    # 20180314 suit for photo raw file: all file has one size
    if key < (32 * 1024 * 1024):
        key = get_hash_key(file)
    else:
        key = str(key)

    after_time = time.time()
    my_output(1, (after_time - before_time))

    return key


def compare_with_binary(left, right):
    if get_file_size(left) != get_file_size(right):
        ptr_str = "exception: key equal and size not equal: %s <--> %s" % (left, right)
        my_output(0, ptr_str)
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
        ptr_str = "\n del \"%s\"\n del \"%s\"\n" % (new_f, old_f)
        my_output(0, ptr_str)
        global _equal_file_num
        _equal_file_num += 1
    else:
        ptr_str = "\n binary not equal, key: %s;\n file: %s\n <--> %s" % (file_key, new_f, old_f)
        my_output(1, ptr_str)


def create_files_dictionary(root_path, file_dict):
    for cur_path, dirs, files in os.walk(root_path):
        for file in files:
            global _total_file_num
            _total_file_num += 1
            if _total_file_num % 10 == 0:
                ptr_str = "\rfile number:%d -->%s" % (_total_file_num, cur_path)
                print(ptr_str, end='', flush=True)

            full_file_name = os.path.join(cur_path, file)
            my_output(1, full_file_name)
            file_key = get_file_key(full_file_name)
            if file_key == 0:
                continue
            if file_key in file_dict:
                process_equal_file(full_file_name, file_dict[file_key], file_key)
            else:
                file_dict[file_key] = full_file_name


def find_entry():
    before = time.time()
    global _total_file_num, _equal_file_num
    _total_file_num = 0
    _equal_file_num = 0
    file_dict = dict()
    create_files_dictionary(r'E:\cartoon', file_dict)

    ptr_str = "\nequal file number:%d\n" % _equal_file_num
    print(ptr_str)
    print_my_output()
    print('totol time:', time.time()-before)


if __name__ == '__main__':
    find_entry()

