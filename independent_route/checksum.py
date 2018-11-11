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

import hashlib
import os


def get_hash(algo):
    if 'md5' in algo:
        return hashlib.md5()
    if 'sha256' in algo:
        return hashlib.sha256()


def check(file, checksum, algo):
    with open(file, 'rb') as f:
        real_hash = get_hash(algo)
        real_hash.update(f.read())
        if real_hash.hexdigest() == checksum:
            return True
        else:
            return False
    return False


def check_all(root, check_sum_file):
    lines = list(open(os.path.join(root, check_sum_file)))
    algo = 'md5'
    for line in lines:
        if 'md5:' in line:
            algo = 'md5'
        elif 'sha256' in line:
            algo = 'sha256'
        elif len(line) > 10:
            full_name = os.path.join(root, line[line.find('*')+1:-1])
            check_sum = line[:line.find(' ')]
            check_pass = check(full_name, check_sum, algo)
            if not check_pass:
                print('Check Failed File:', full_name)


def check_file():
    file = r'C:\Users\CHM\Downloads\Everything-1.4.1.895.x64.zip'
    checksum = 'e7c0e506b9c308f3d1857288855eeda6d8ec3504b3a7f01474c5dcea495ab9d9'
    rc = check(file, checksum, 'sha256')
    if rc:
        print('Check Pass!')
    else:
        print('CheckFiled')


if __name__ == '__main__':
    check_file()
    #root = r'E:\weiyun\python'
    #check_sum_file = 'checksum.txt'
    #check_all(root, check_sum_file)
