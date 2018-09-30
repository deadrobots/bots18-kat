#!/usr/bin/python
import os, sys
from wallaby import *
import actions as a
import drive as d
import utils as u
import constants as c



def main():
    print("Hello Kat")
    a.init()
    d.timedLineFollow(5)



if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();



#Need to check that the rotate print statement works
#Need to check that the drive distance function works with different speeds and in negative direction