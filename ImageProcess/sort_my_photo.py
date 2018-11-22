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
#  2018.11.22 init
from ImageProcess.ImageInfo import PhotoInfo
from ImageProcess.CameraType import g_CameraTypeConverter


#  --- year
#  ------ month
#  --------- camera type

class SortPhoto:
    def __init__(self):
        pass

    def process(self, root):
        pass


if __name__ == '__main__':
    p = PhotoInfo(r'E:\picture\IMG_20181120_181951.jpg')
    print(g_CameraTypeConverter.get(p.get_camera_type()))

