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

import os
import hashlib
import time


_total_file_num = 0
_equal_file_num = 0


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
    if key < (8 * 1024 * 1024):
        key = get_hash_key(file)

    after_time = time.time()
    if False:
        print(after_time - before_time)

    return key


def process_equal_file(new_f, old_f):
    print(new_f, old_f)
    global _equal_file_num
    _equal_file_num += 1


def create_files_dictionary(root_path, file_dict):
    for cur_path, dirs, files in os.walk(root_path):
        for file in files:
            global _total_file_num
            _total_file_num += 1
            if _total_file_num % 10000 == 0:
                print("file num:", _total_file_num)

            full_file_name = os.path.join(cur_path, file)
            # print(full_file_name)
            file_key = get_file_key(full_file_name)
            if file_key in file_dict:
                process_equal_file(full_file_name, file_dict[file_key])
            else:
                file_dict[file_key] = full_file_name


def find_entry():
    global _total_file_num, _equal_file_num
    _total_file_num = 0
    _equal_file_num = 0
    file_dict = dict()
    create_files_dictionary('e:/', file_dict)

    print("equal file num:", _equal_file_num)


if __name__ == '__main__':
    find_entry()
