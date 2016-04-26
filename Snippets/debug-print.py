#!/usr/bin/env python
# -*- coding: utf-8 -*-

DEBUGLEVEL = 1

def dbgout(lvl, *args):
    """ Conditionally print 'args' if global 'DEBUGLEVEL' is equal to parameter 'lvl' """
    if lvl == DEBUGLEVEL: # This should make it very easy to disable many debug statements at once
        print "DEBUG:",
        for arg in args:
            print arg,
        print
        
if True:
    dbgout(1, 'Printing a bebug message for level', DEBUGLEVEL)