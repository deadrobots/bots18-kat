#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import utils as u
import math



#Wheel Values
diam = 2.6875
circum = diam * math.pi
#dist =
rot = 3815 #number of ticks to rotate 360


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


def driveDistance(lspeed, rspeed, distance):
    print 'Driving',distance,'inches'
    clear_motor_position_counter(c.LMOTOR)
    ticks = distance * ticksPerInch
    if ticks > 0:
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
    clear_motor_position_counter(c.LMOTOR)
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
    print(get_motor_position_counter(c.LMOTOR))

# Great job using motor ticks to precisely turn.
# I suggest not using any timed-drive functions, as that will decrease the accuracy of
# your turn. You don't need to pay attention to time if you are looking at motor ticks
# to tell you how far you have turned. -LMB
def rotateSpeed(degree, speed):
    print 'Rotating', degree, 'degrees'
    clear_motor_position_counter(c.LMOTOR)
    clear_motor_position_counter(c.RMOTOR)
    ticks = (rot * degree) / 395
    if ticks < 0:
        ticks = ticks * -1
    if degree < 0:	# You can turn this into one single while loop, for increased code 
					# readability and maintainability. -LMB
        while (get_motor_position_counter(c.LMOTOR) < ticks):
            driveTimed(speed, -int(speed * 0.94), 10)
    elif degree > 0:
        while (get_motor_position_counter(c.RMOTOR) < ticks):
            driveTimed(-(speed), int(speed * 0.94), 10)
    elif degree is 0:
        pass
    motor(c.LMOTOR, 0)
    motor(c.RMOTOR, 0)
    msleep(10) 	# this function does not need a final msleep() command. The code that calls this 
				# function might, but it also might hinder your robot if it was called frequently
				# from within a loop. This might sound nit-picky for just 10 milliseconds, but
				# it can add up  -LMB


def lineFollowUntilCan():
    clear_motor_position_counter(c.LMOTOR)
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


