#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# (c) Vinay <vchandra@tcd.ie>

import sys
sys.path.append('../src')
from haversine import distanceInKM


def main():
    l1 = (52.2296756, 21.0122287)
    l2 = (52.406374, 16.9251681)

    d = distanceInKM(l1, l2)

    if int(d) == 278:
        print("Test passed for Calculating haversine distance")
    else:
        print("Error in Haversine distance function")


if __name__ == '__main__':
    main()
