#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import utils as u
import math



#Wheel Values
diam = 2.6875
circum = diam * math.pi


#Tick Values
tickPerRotate = 1880
#number of inches per rotation = 8.443
ticksPerInch = 222.67



def drive(lspeed, rspeed):
    motor(c.LMOTOR, lspeed)
    motor(c.RMOTOR, rspeed)


def driveTimed(lspeed, rspeed, time):
    motor(c.LMOTOR, lspeed)
    motor(c.RMOTOR, rspeed)
    msleep(time)
    motor(c.LMOTOR, 0)
    motor(c.RMOTOR, 0)
    msleep(10)

# I also like this code. I am curious to see how straight it can drive. -LMB
def driveDistance(lspeed, rspeed, distance):
    print 'Driving',distance,'inches'
    clear_motor_position_counter(c.LMOTOR)
    ticks = distance * ticksPerInch
    if (ticks > 0): # Parentheses here are not required (my apologies. I messed up on the documentation paper I gave you) -LMB
        motor(c.LMOTOR, lspeed)
        motor(c.RMOTOR, rspeed)
        while (get_motor_position_counter(c.LMOTOR) < ticks):
            pass
        motor(c.LMOTOR, 0)
        motor(c.RMOTOR, 0)
        msleep(10)
    else:
        motor(c.LMOTOR, -lspeed)
        motor(c.RMOTOR, -rspeed)
        while (get_motor_position_counter(c.LMOTOR) > ticks):
            pass
        motor(c.LMOTOR, 0)
        motor(c.RMOTOR, 0)
        msleep(10)


def arc(degree):
    time = degree * 13
    if time < 0:
        time = time * -1
    if degree < 0:
        motor(c.LMOTOR, 100)
        motor(c.RMOTOR, 0)
        msleep(time + 50)
    elif degree > 0:
        motor(c.LMOTOR, 0)
        motor(c.RMOTOR, 100)
        msleep(time)
    elif degree is 0:
        pass
    motor(c.LMOTOR, 0)
    motor(c.RMOTOR, 0)
    msleep(10)


def rotate(degree):
    print 'Rotating',degree,'degrees'
    time = degree * 8
    if time < 0:
        time = time * -1
    if degree < 0:
        motor(c.LMOTOR, 84)
        motor(c.RMOTOR, -79) # These hard-coded values seem fishy to me...
        msleep(time)		# perhaps they should be defined as constants (or ideally, based upon
    elif degree > 0:		# the calculated difference between each wheel that you've determined
        motor(c.LMOTOR, -84)# for the other drive functions -LMB
        motor(c.RMOTOR, 79)
        msleep(time)
    elif degree is 0:
        pass
    motor(c.LMOTOR, 0)
    motor(c.RMOTOR, 0)
    msleep(10)


def lineFollowUntilCan(): # Does this work along that first large turn on the mat? The drive turn values don't
    clear_motor_position_counter(c.LMOTOR) # appear to be spaced widely enough from each other. -LMB
    while analog(c.ET) < c.seeCan:
        if u.onBlack():
            drive(80, 60)
            msleep(10)
        else:
            drive(60, 80)
            msleep(10)
    print("saw can")
    driveTimed(0, 0, 500)


def lineFollowDistance(inches):
    clear_motor_position_counter(c.LMOTOR)
    while (ticksPerInch * inches) > get_motor_position_counter(c.LMOTOR):
        if u.onBlack():
            drive(80, 70)
            msleep(10)
        else:
            drive(70, 80)
            msleep(10)
    driveTimed(0, 0, 500)


def smoothTimedLineFollow(sec, speed):
    stopTime = seconds() + sec
    while seconds() < stopTime:
        if u.onBlack():
            drive(speed, speed - 10)
            msleep(10)
        else:
            drive(speed - 10, speed)
            msleep(10)
    driveTimed(0, 0, 500)


def timedLineFollow(sec, speed):
    stopTime = seconds() + sec
    if speed < 30:
        speed = 30
    else:
        pass
    while seconds() < stopTime:
        if u.onBlack():
            drive(speed, speed - 30)
            msleep(10)
        else:
            drive(speed - 30, speed)
            msleep(10)
    driveTimed(0, 0, 500)


