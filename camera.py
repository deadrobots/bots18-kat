#!/usr/bin/python
import os, sys
from wallaby import *
import drive as d
import constants as c
import utils as u



cameraWidth = 160
cameraHeight = 120


def spinUntilColorPositive(color):
    camera_update()
    msleep(2000)
    while get_object_count(color) == 0:
        camera_update()
        msleep(100)
        d.rotate(1)
    print("saw object")
    msleep(500)
    while get_object_center_x(color, 0) < 80:
        print(get_object_center_x(color, 0))
        camera_update()
        msleep(100)
        d.rotate(1)


def spinUntilColorNegative(color):
    camera_update()
    msleep(2000)
    while (get_object_count(color) == 0) and (get_object_area(color, 0) > 100):
        camera_update()
        msleep(100)
        d.rotate(-1)
    print("saw object")
    msleep(500)
    print(get_object_center_x(color, 0))