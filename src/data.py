#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# (c) Vinay <vchandra@tcd.ie>

import json
from config import DATASET_PATH


def isBlank(myString):
    return not(myString and myString.strip())


def readData():
    filename = DATASET_PATH
    # Reading dataset lines
    with open(filename) as f:
        lines = f.readlines()
    processedData = {}
    for line in lines:
        j = json.loads(line)
        # Check for latitude and longitude values for users else return
        if isBlank(j['latitude']) or isBlank(j['longitude']):
            print(j['user_id'] + "is Incomplete, Please fill the missing data")
        processedData[j['user_id']] = [j['name'], (float(j['latitude']),
                                                   float(j['longitude']))]
    return processedData
