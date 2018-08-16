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
# import time


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


def binary_equal(left, right):
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


class DirectoryHash:
    def __init__(self, root):
        self._root = root
        self._dict = dict()
        self._conflict = []

    def add_conflict_info(self, l_f, r_f):
        info = '\nrm %s\n # %s' % (l_f, r_f)
        self._conflict.append(info)

    def run(self):
        for cur_path, dirs, files in os.walk(self._root):
            for file in files:
                full_path = os.path.join(cur_path, file)
                key = get_file_key(full_path)
                if key == 0:
                    continue

                if key in self._dict:
                    self.first_equal(full_path, self._dict[key])
                else:
                    self._ref_dict[key] = full_path

    def first_equal(self, cur_file, dict_file):
        if binary_equal(cur_file, dict_file):
            self.add_conflict_info(cur_file, dict_file)
        else:
            key = get_hash_key(cur_file)
            if key in self._dict:
                assert False
            else:
                self._dict[key] = cur_file


class CmpDirectory:
    def __init__(self, del_resit, ref_dir, to_check_dir):
        self._del_resit = del_resit
        self._ref_dir = ref_dir
        self._to_check_dir = to_check_dir

        self._ref_dict = dict()
        self._to_check_dict = dict()
        self._ref_conflict_info = []
        self._to_check_conflict_info = []

    def run(self):
        self.build_ref_dict()
        if self._del_resit:
            self.check_and_del()
        else:
            self.only_check()

    def build_ref_dict(self):
        for cur_path, dirs, files in os.walk(self._ref_dir):
            for file in files:
                full_path = os.path.join(cur_path, file)
                key = get_file_key(full_path)
                if key in self._ref_dict:
                    self.first_conflict(key, full_path)
                else:
                    self._ref_dict[key] = full_path

    @staticmethod
    def first_conflict(key, full_path, t_dict, t_info):
        """
        if key
        :param key:
        :param full_path:
        :param t_dict:
        :param t_info:
        :return:
        """
        if key == str(get_file_size(full_path)):
            new_key = get_hash_key(full_path)
            if new_key not in t_dict:
                t_dict[new_key] = full_path
                return

        compare

    def check_and_del(self):
        pass

    def only_check(self):
        pass

    def create_ref_conflict_info(self, l_file, r_file):
        pass

    def create_to_check_conflict_info(self, l_file, r_file):
        pass

    @staticmethod
    def delete_to_check_conflict_file(file):
        os.remove(file)




def cmp_entity():
    pass


if __name__ == '__main__':
    cmp_entity()
