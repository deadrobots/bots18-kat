#!/usr/bin/python
import os, sys
from wallaby import *



#Analog Ports:

topHat = 0
ET = 5

#Motor Ports:

RMOTOR = 0
LMOTOR = 3


#Servo Ports:
servoArm = 0
servoClaw = 1

#Camera Channels:
RED = 0
GREEN = 1
BLUE = 2
ORANGE = 3

#Servo Positions:
#Arm
armUp = 2047
armLevel = 1050
armCan = 900
armDown = 775

#Claw
clawOpen = 2047
clawOpen90 = 1650
grabCan = 1100
clawClosed = 900

black = 1500
seeCan = 1900