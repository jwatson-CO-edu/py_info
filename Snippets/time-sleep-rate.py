#!/usr/bin/env python

"""
RESULT:
"""

import time

class HeartRate: # NOTE: This fulfills a purpose similar to the rospy rate
    """ Sleeps for a time such that the period between calls to sleep results in a frequency not greater than the specified 'Hz' """
    def __init__( self , Hz ):
        """ Create a rate object with a Do-Not-Exceed frequency in 'Hz' """
        self.period = 1.0 / Hz; # Set the period as the inverse of the frequency , hearbeat will not exceed 'Hz' , but can be lower
        self.last = time.time()
    def sleep( self ):
        """ Sleep for a time so that the frequency is not exceeded """
        elapsed = time.time() - self.last
        if elapsed < self.period:
            time.sleep( self.period - elapsed )
        self.last = time.time()
        
rate = HeartRate( 0.1 ) # Create a rate object with 0.1 Hz , period of 10s

last = time.time()
rate.sleep()
print time.time() - last
last = time.time()
rate.sleep()
print time.time() - last