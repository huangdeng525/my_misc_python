#!/usr/bin/python3
# -*- coding: utf-8 -*-
# calc_distance.py
#
# calc_distance
#
#  Copyright (C) 2019-2019 huangdeng @ chengdu
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  2019.09.02 init
import math

# to change
sat_longitude = 10

# include earth radius
earth_radius = 6378
sat_high = 35768 + earth_radius


def cal_disatance(latitude, longitude):
    # Step 1) Determine the diﬀerential longitude, B, Eq. (2.10):
    B = longitude - sat_longitude

    # Step 2) Determine the earth radius at the earth station, R, for the calculation of the range Eqs. (2.11) to (2.13):
    e = (earth_radius / math.sqrt(1 - 0.08182 * 0.08182 * math.sin(longitude) * math.sin(longitude)) + 0) * math.cos(longitude)
    z = (earth_radius * (1 - 0.08182 * 0.08182) / math.sqrt(1 - 0.08182 * 0.08182 * math.sin(longitude) * math.sin(longitude)) + 0) * math.sin(longitude)
    fin_e = math

    # Step 3) Determine the range d, Eq. (2.15):
    d = math.sqrt(earth_radius * earth_radius + sat_high * sat_high - 2 * earth_radius * sat_high * math.cos() * math.cos(B)) 



def calc():
    latitude = 0
    longitude = 0

