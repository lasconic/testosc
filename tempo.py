""" A quick OSC test. """

import sys
# JOA: import SimpleOSC
from simpleOSC import *
from time import time

# opening an OSC socket to a computer running MuseScore with OSC
def main(*args):
    #print args[1]
    initOSCClient('localhost', 5282)
    t0 = time()
    while 1:
        
        raw_input("Press space")
        t1 = time()
        t = 60 / (t1-t0) 
        print t
        t0 = t1
        sendOSCMsg( '/tempo', [int(t)])
    
    
    
    closeOSC()

 
if __name__ == '__main__':
    sys.exit(main(*sys.argv))


