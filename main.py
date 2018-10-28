#!/usr/bin/python
import os, sys
from wallaby import *
import actions as a
import drive as d
import utils as u
import constants as c
import camera as x



def main():
    print("Hello Kat")
    a.init()
    x.spinUntilColorPositive(c.RED)




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();



#configured camera
#need to work on camera functions
#need to work on a proportion line follow
#next task: pom chase