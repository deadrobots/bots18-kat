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
    a.findCanDeliverHome()




if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();



#need to configure camera
#need to work on a proportion line follow
#next task: pom chase