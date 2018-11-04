#!/usr/bin/python
import os, sys
from wallaby import *
import drive as d
import utils as u
import constants as c
import camera as x


def init():
    print("opening camera")
    camera_open_black()
    msleep(3000)
    print("opened camera")
    camera_update()
    print("updated camera")
    msleep(2000)
    enable_servo(c.servoArm)
    enable_servo(c.servoClaw)
    u.moveServo(c.servoClaw, c.clawOpen90, 10)
    u.moveServo(c.servoArm, c.armLevel, 10)


def driveSquare(size):
    '''x = 4
    while x > 0:
        driveTimed(100, 100, size)
        rotate(90)
        msleep(500)
        x -= 1'''
    size = size * 1000
    for x in range(0, 4):
        d.driveTimed(80, 80, size)
        msleep(200)
        d.rotate(90)
        msleep(200)


def grabCan():
    u.moveServo(c.servoClaw, c.clawOpen, 20)
    msleep(200)
    u.moveServo(c.servoArm, c.armLevel, 20)
    msleep(500)
    d.driveTimed(80, 80, 1000)
    u.moveServo(c.servoClaw, c.clawOpen90, 10)
    u.moveServo(c.servoClaw, c.grabCan, 5)
    msleep(200)
    u.moveServo(c.servoArm, 1200, 10)


def lFUntilCan():
    #line follows until can, grabs can, rotates 90, then drops can
    print("looking for can")
    u.moveServo(c.servoArm, c.armCan, 20)
    u.moveServo(c.servoClaw, c.clawOpen90 - 100, 20)
    d.lineFollowUntilCan()
    print("saw can")
    u.moveServo(c.servoClaw, c.grabCan, 5)
    msleep(200)
    u.moveServo(c.servoArm, 1200, 10)
    msleep(200)
    d.rotate(-90)
    u.moveServo(c.servoArm, c.armCan, 20)
    u.moveServo(c.servoClaw, c.clawOpen90, 20)


def findCanDeliverHome():
    print("looking for can")
    u.moveServo(c.servoArm, c.armCan, 20)
    u.moveServo(c.servoClaw, c.clawOpen90 - 100, 20)
    startTime = seconds()
    d.lineFollowUntilCan()
    totalTime = seconds() - startTime
    u.moveServo(c.servoClaw, c.grabCan, 5)
    msleep(200)
    u.moveServo(c.servoArm, 1200, 10)
    msleep(200)
    d.rotate(190)
    u.waitForButton()
    d.smoothTimedLineFollow(totalTime)




