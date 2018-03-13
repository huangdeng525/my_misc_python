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


import os
import hashlib


def get_hash_key(file):
    myhash = hashlib.sha1()
    f = open(file, 'rb')

    while True:
        b = f.read(4096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


def get_size_key(file):
    pass


def get_file_key(file):
    if True:
        return get_hash_key(file)
    else:
        return get_size_key()


def create_files_dictionary(root_path, file_dict):
    for cur_path, dirs, files in os.walk(root_path):
        for file in files:
            full_file_name = os.path.join(cur_path, file)
            #print(full_file_name)
            file_key = get_file_key(full_file_name)
            if file_key in file_dict:
                print(full_file_name, file_dict[file_key])
            else:
                file_dict[file_key] = full_file_name


def find_entry():
    file_dict = dict()
    create_files_dictionary('e:\code', file_dict)


if __name__ == '__main__':
    find_entry()
