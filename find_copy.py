#!/usr/bin/python3
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

import os
import hashlib
import time


_total_file_num = 0
_equal_file_num = 0
_debug_flag_ = False


def my_output(level, prt_str):
    if level == 0:
        print(prt_str)
    if level == 1 and _debug_flag_:
        print(prt_str)


def get_hash_key(file):
    my_hash = hashlib.sha1()
    f = open(file, 'rb')

    while True:
        b = f.read(4096)
        if not b:
            break
        my_hash.update(b)
    f.close()
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
    # if file size over 8M, then use file size as key
    # 20180314 suit for photo raw file: all file has one size
    if key < (32 * 1024 * 1024):
        key = get_hash_key(file)

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
        ptr_str = "binary equal, key: 0x%x; file: %s <--> %s" % (file_key, new_f, old_f)
        my_output(0, ptr_str)
        global _equal_file_num
        _equal_file_num += 1
    else:
        ptr_str = "binary not equal, key: 0x%x; file: %s <--> %s" % (file_key, new_f, old_f)
        my_output(1, ptr_str)


def create_files_dictionary(root_path, file_dict):
    for cur_path, dirs, files in os.walk(root_path):
        for file in files:
            global _total_file_num
            _total_file_num += 1
            if _total_file_num % 10000 == 0:
                ptr_str = "file number:%d" % _total_file_num
                my_output(1, ptr_str)

            full_file_name = os.path.join(cur_path, file)
            my_output(1, full_file_name)
            file_key = get_file_key(full_file_name)
            if file_key in file_dict:
                process_equal_file(full_file_name, file_dict[file_key], file_key)
            else:
                file_dict[file_key] = full_file_name


def find_entry():
    global _total_file_num, _equal_file_num
    _total_file_num = 0
    _equal_file_num = 0
    file_dict = dict()
    create_files_dictionary('E:\\test', file_dict)

    ptr_str = "equal file number:%d" % _equal_file_num
    my_output(0, ptr_str)


if __name__ == '__main__':
    find_entry()

