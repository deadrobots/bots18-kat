#!/usr/bin/python
import os, sys
from wallaby import *
import drive as d
import constants as c



def waitForButton():
    print("waiting for right button")
    while right_button() == 0:
        pass
    print("right button pressed")
    msleep(500)


def moveServo(servo, position, speed):
    i = get_servo_position(servo)
    if position > i:
        while i < position:
            set_servo_position(servo, i)
            i += speed
            msleep(10)
        set_servo_position(servo, position)
    else:
        while i > position:
            set_servo_position(servo, i)
            i -= speed
            msleep(10)
        set_servo_position(servo, position)


def onBlack():
    if analog(c.topHat) > c.black:
        return True
    else:
        return False
