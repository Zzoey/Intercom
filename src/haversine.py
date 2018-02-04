#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# (c) Vinay <vchandra@tcd.ie>

from math import sin, cos, sqrt, atan2, radians


def distanceInKM(origin, var):
    # origin - Intercom Dublin GPS Co-ordinates
    # var : Customer Co-ordinates
    oLat, oLon = origin
    pLat, pLon = var

    # Approximate Radius of Earth in KM
    R = 6371.0
    deltaLon = radians(pLon - oLon)
    deltaLat = radians(pLat - oLat)

    p = sin(deltaLat/2)**2 + cos(radians(oLat)) \
        * cos(radians(pLat)) * sin(deltaLon/2)**2

    deltaSigma = 2 * atan2(sqrt(p), sqrt(1-p))
    # haversine distance between two GPS co-ordinates
    return R * deltaSigma
