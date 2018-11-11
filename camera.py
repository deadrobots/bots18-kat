#!/usr/bin/python
import os, sys
from wallaby import *
import drive as d
import constants as c
import utils as u



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


def driveToColor(color):
    print("Running drive to color function")
    camera_update()
    msleep(2000)
    while get_object_count(color) == 0:
        camera_update()
        msleep(100)
        d.rotate(1)
    print("saw object")
    msleep(500)
	# Note that the "center" of your x/y camera view is actually around 80.
	# The furthest-left value is 0, the furthest right value is around 160
	# As it is written, I would expect your code to attempt to keep the can in the
	# "corner" of your robot's vision, as it moves towards it. 5 and 15 are not
	# good values for "centering" the can -LMB
    while (get_object_center_x(color, 0) > 15) or (get_object_center_x(color, 0) < 5):
        print(get_object_center_x(color, 0))
        camera_update()
        msleep(100)
        if get_object_center_x(color, 0) < 5:
            d.rotate(-1)
        elif get_object_center_x(color, 0) > 15:
            d.rotate(1)
    print("Centered can")
    print(get_object_center_x(color, 0))
    msleep(500)
    while get_object_center_y(color, 0) < 60:
        print(get_object_center_y(color, 0))
        d.driveTimed(10, 10, 20)
    print("Got close to can")