#!/usr/bin/python3
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


class MyLocker:
    def __init__(self):
        pass

    def lock(self):
        pass

    def unlock(self):
        pass


# multi instance
class ConflictFile:
    def __init__(self):
        self._record = []

    def add(self, info):
        self._record.append(info)

    def output(self):
        for one_info in self._record:
            print(one_info)


# one instance
class FileCollect:
    """docstring for FileCollect"""
    def __init__(self, obj_lock):
        self._obj_lock = obj_lock
        self._files = []

    def add(self, fullname):
        """call by single thread"""
        self._files.append(fullname)

    def get(self)
        """call by multi thread"""
        self._obj_lock.lock()
        # pop one file

        self._obj_lock.unlock()


# multi instance
class CalcHash():
    """docstring for CalcHash"""
    def __init__(self, files, confict_recorder):
        self._files = files
        self._myrecord = dict()
        self._confict = confict_recorder
        self._file = []
        self._key = []

    def run(self)
        while True:
            self._file = self._files.get()
            if self._file:
                self.calc(self._file)
                self.record()
            else:
                break

    def calc(self, one_file)
        pass

    def record(self, key)
        if self._key in self._myrecord:
            self.record_same_info(self._file, self._myrecord[self._key])
        else:
            self._myrecord[self._key] = self._file
            