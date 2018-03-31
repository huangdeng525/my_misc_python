#!/usr/bin/python3
# -*- coding: utf-8 -*-
# find_copy.py
# 
#  find the equal file in filesystem, multi threading version
# 
#  Copyright (C) 2018-2018 huangdeng @ chengdu
# 
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  2018.3.24 init 

# design:
# step 1: collect all file's name by single thread
# step 2: calc hash by multi thread
# step 3: assemble the result

__author__ = 'huangdeng'

import hashlib
import concurrent.futures
import os
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
        # ptr_str = "exception: key equal and size not equal: %s <--> %s" % (left, right)
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


class FindEqual:
    def __init__(self, root):
        self._root = root
        self._files = []
        self._dict = dict()
        self._equal_file = 0
        self._total_file = 0
        self._out = []

    def collect_files(self):
        for cur_path, dirs, files in os.walk(self._root):
            for file in files:
                full_path = os.path.join(cur_path, file)
                if (1024*1024) < get_file_size(full_path) < (32 * 1024 * 1024):
                    self._files.append(full_path)
                else:
                    self.inc()
                    key = get_file_key(full_path)
                    self.inset_key(key, full_path)

    def parallel_get_key(self):
        print('total collect file number:', len(self._files))
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for file, file_key in zip(self._files, executor.map(get_file_key, self._files)):
                self.inc()
                # if self._total_file % 10 == 0:
                # ptr_str = "\rfile number:%d -->%s" % (self._total_file, file)
                # print(ptr_str, end='', flush=True)

                self.inset_key(file_key, file)

    def inset_key(self, file_key, file):
        if file_key == 0:
            return
        if file_key in self._dict:
            self.process_equal_file(file, self._dict[file_key], file_key)
        else:
            self._dict[file_key] = file

    def run(self):
        self.collect_files()
        self.parallel_get_key()
        for one in self._out:
            print(one)
        print('equal file number:', self._equal_file, 'total file number:', self._total_file)

    def process_equal_file(self, new_f, old_f, file_key):
        if compare_with_binary(new_f, old_f):
            ptr_str = "\n binary equal, key: %s;\n file: %s\n    <--> %s" % (file_key, new_f, old_f)
            self._out.append(ptr_str)
            self._equal_file += 1
        else:
            #ptr_str = "\n binary not equal, key: %s;\n file: %s\n <--> %s" % (file_key, new_f, old_f)
            #self._out.append(ptr_str)
            pass

    def inc(self):
        self._total_file += 1
        if self._total_file % 10 == 0:
            ptr_str = "\rfile number:%d" % self._total_file
            print(ptr_str, end='', flush=True)


def find_entry():
    before = time.time()
    process = FindEqual(r'F:\photo\canon')
    process.run()
    print('total time:', time.time() - before)


if __name__ == '__main__':
    find_entry()
