""" A quick OSC test. """

import sys
# JOA: import SimpleOSC
from simpleOSC import *

# opening an OSC socket to a computer running MuseScore with OSC
def main(*args):
    #print args[1]
    initOSCClient('localhost', 5282)

    # sendOSCMsg( '/actions/note-c')
    # sendOSCMsg( '/actions/pad-note-2')
    # sendOSCMsg( '/actions/note-a')
    # sendOSCMsg( '/actions/pad-note-4')
    # sendOSCMsg( '/actions/note-c')
    # sendOSCMsg( '/actions/note-b')
    sendOSCMsg( '/actions/play')
    closeOSC()

 
if __name__ == '__main__':
    sys.exit(main(*sys.argv))


