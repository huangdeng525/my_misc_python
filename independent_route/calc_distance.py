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
sat_longitude = 126.4
earth_latitude = 39.9
earth_longitude = 116.4

# include earth radius
earth_radius = 6378
sat_high = 35786 + earth_radius

max_distance = 300000 * 0.003


const_parameter = 0.01745
def cal_distance_e(latitude, longitude):
    # Step 1) Determine the diﬀerential longitude, B, Eq. (2.10):
    B = longitude - sat_longitude

    # used const_parameta
    d = math.sqrt(earth_radius * earth_radius + sat_high * sat_high - 2 * earth_radius * sat_high * math.cos(latitude*const_parameter) * math.cos(B*const_parameter))
    return d


def cal_distance(latitude, longitude):
    return cal_distance_e(latitude, longitude)
    # Step 1) Determine the diﬀerential longitude, B, Eq. (2.10):
    B = longitude - sat_longitude

    # Step 2) Determine the earth radius at the earth station, R, for the calculation of the range Eqs. (2.11) to (2.13):
    e = (earth_radius / math.sqrt(1 - 0.08182 * 0.08182 * math.sin(longitude) * math.sin(longitude)) + 0) * math.cos(longitude)
    z = (earth_radius * (1 - 0.08182 * 0.08182) / math.sqrt(1 - 0.08182 * 0.08182 * math.sin(longitude) * math.sin(longitude)) + 0) * math.sin(longitude)
    fin_e = math

    # Step 3) Determine the range d, Eq. (2.15):
    d = math.sqrt(earth_radius * earth_radius + sat_high * sat_high - 2 * earth_radius * sat_high * math.cos() * math.cos(B))


def calc_boundary_lat(start_latitude, ref_longitude, central_point_distance):
    flag = False
    finded = False
    latitude = start_latitude
    for x in range(180):
        distance = cal_distance(latitude + 1, ref_longitude)
        if abs(distance - central_point_distance) <= max_distance:
            flag = True
        if abs(distance - central_point_distance) > max_distance:
            if flag:
                finded = True
            break
        latitude += 1

    n_flag = False
    n_finded = False
    n_latitude = start_latitude
    for x in range(180):
        distance = cal_distance(n_latitude - 1, ref_longitude)
        if abs(distance - central_point_distance) <= max_distance:
            n_flag = True
        if abs(distance - central_point_distance) > max_distance:
            if n_flag:
                n_finded = True
            break
        n_latitude -= 1

    if finded and n_finded:
        return [True, [latitude, n_latitude]]

    return [False, [0,0]]


def calc_boundary_long(start_longitude, ref_latitude, central_point_distance):
    flag = False
    finded = False
    longitude = start_longitude
    for x in range(180):
        distance = cal_distance(ref_latitude, longitude + 1)
        if abs(distance - central_point_distance) <= max_distance:
            flag = True
        if abs(distance - central_point_distance) > max_distance:
            if flag:
                finded = True
            break
        longitude += 1

    n_flag = False
    n_finded = False
    n_longitude = start_longitude
    for x in range(180):
        distance = cal_distance(ref_latitude, n_longitude - 1)
        if abs(distance - central_point_distance) <= max_distance:
            n_flag = True
        if abs(distance - central_point_distance) > max_distance:
            if n_flag:
                n_finded = True
            break
        n_longitude -= 1

    if finded and n_finded:
        return [True, [longitude, n_longitude]]

    return [False, [0,0]]


def calc():
    # step 1 ??????????????
    central_point_distance = cal_distance(earth_latitude, earth_longitude)
    ref_latitude = int(earth_latitude)
    ref_longitude = int(earth_longitude)

    # step 2 ???1?????????max_distance?????
    result_points = []

    result = calc_boundary_long(ref_longitude, ref_latitude, central_point_distance)
    if not result[0]:
        return []

    for x in range(result[1][1], result[1][0]):
        point = calc_boundary_lat(ref_latitude, x, central_point_distance)
        if point[0]:
            result_points.append([x, point[1][0], point[1][1]])


    return result_points


if __name__ == '__main__':
    print(calc())
