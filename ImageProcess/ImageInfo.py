#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ImageInfo.py
#
# picture info base function
#
#  Copyright (C) 2018-2018 huangdeng @ chengdu
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  2018.11.22 init

import exifread


class PhotoInfo:
    def __init__(self, in_file):
        with open(in_file, mode='rb') as f:
            self._tags = exifread.process_file(f)
            print(self._tags)

    def get_camera_type(self):
        if 'Image Model' in self._tags:
            return self._tags['Image Model'].values
        return None

    def get_take_time(self):
        if 'Image DateTime' in self._tags:
            return self._tags['Image DateTime'].values
        return None

    def get_size(self):
        if 'Image ImageWidth' in self._tags:
            return self._tags['Image ImageWidth'].values[0], self._tags['Image ImageLength'].values[0]
        elif 'Image' in self._tags:
            return self._tags['Width'].values[0], self._tags['Height'].values[0]
        return None


def get_photo_info(in_file):
    """
    :param in_file:
    :return: camera type, time, size[x, y]

    camer type:
        Image Model : LLD-AL20

    time:
        Image DateTime : 2018:11:20 18:19:51

    photo pixel size:
        Image ImageWidth : 4160
        Image ImageLength : 3120
    """
    with open(in_file, mode='rb') as f:
        tags = exifread.process_file(f)
        return tags['Image Model'], tags['Image DateTime'], [tags['Image ImageWidth'], tags['Image ImageLength']]


if __name__ == '__main__':
    camera_type, take_time, photo_size = get_photo_info(r'E:\picture\IMG_20181120_181951.jpg')
    print(camera_type, take_time, photo_size[0], photo_size[1])
    p = PhotoInfo(r'E:\picture\IMG_20181120_181951.jpg')
    print(type(p.get_camera_type()))
    print(type(p.get_take_time()))
    x, y = p.get_size()
    print(type(x), type(y))
    print(x * y)
