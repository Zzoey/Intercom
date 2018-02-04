#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# (c) Vinay <vchandra@tcd.ie>

from collections import OrderedDict
from haversine import distanceInKM
from data import readData
import sys


sys.dont_write_bytecode = True
result = {}


def main():
    # Intercom Office GPS co-ordinates
    origin = (53.3381985, -6.2592576)
    processedData = readData()
    for key, value in processedData.items():
        name = value[0]
        gpsValues = value[1]
        d = distanceInKM(origin, gpsValues)
        if d < 100.0:
            result[key] = name
    finalResult = OrderedDict(sorted(result.items()))

    for key in finalResult:
        print(key, ':', finalResult[key])

    print('There are ' + str(len(finalResult)) + ' people within 100'
          ' Km radius from Intercom.')


if __name__ == '__main__':
    main()
