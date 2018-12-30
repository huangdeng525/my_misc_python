#!/usr/bin/python3
# -*- coding: utf-8 -*-
# sort_my_photo.py
#
# Sort photos by format
#
#  Copyright (C) 2018-2018 huangdeng @ chengdu
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  2018.11.30 init

import os

from ImageProcess.ImageInfo import PhotoInfo
from ImageProcess.CameraType import g_CameraTypeConverter


class AllType:
    def __init__(self, root_dir):
        self._all_type = dict()
        self._root = root_dir

    def out(self):
        for cur_path, dirs, files in os.walk(self._root):
            for file in files:
                if '.jpg' in file or '.arw' in file:
                    fullname = os.path.join(cur_path, file)
                    p = PhotoInfo(fullname)
                    camera_type = p.get_camera_type()
                    if camera_type not in self._all_type:
                        print(camera_type, fullname)
                        self._all_type[camera_type] = 0
                    else:
                        self._all_type[camera_type] = self._all_type[camera_type]+1


if __name__ == '__main__':
    p = AllType('F:\SE\photo')
    p.out()
