#!/usr/bin/python3
# -*- coding: utf-8 -*-
# sort_by_size.py
#
# Sort photos by size
#
#  Copyright (C) 2019-2019 huangdeng @ chengdu
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  2019.01.28 init

import shutil
import os
from PIL import Image

_small_size = 640 * 480
_small_dir = 'D:\small'
_middle_size = 1024 * 768
_middle_dir = 'D:\middle'
_large_dir = 'D:\large'

def get_img_size(file):
    img = Image.open(file)
    return img.size[0] * img.size[1]


def sort_by_size(root):
    for cur_path, dirs, files in os.walk(root):
        for file in files:
            if '.jpg' == file[-4:]:
                ori_file = os.path.join(cur_path, file)
                size = get_img_size(ori_file)
                if size < _small_size:
                    print('move:', ori_file, 'to small')
                    shutil.copy(ori_file, _small_dir)
                elif size < _middle_size:
                    print('move:', ori_file, 'to middle')
                    shutil.copy(ori_file, _middle_dir)
                else:
                    print('move:', ori_file, 'to large')
                    shutil.copy(ori_file, _large_dir)


if __name__ == '__main__':
    sort_by_size('D:\9ipic')
