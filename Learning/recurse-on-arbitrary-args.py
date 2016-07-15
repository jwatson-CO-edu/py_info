# -*- coding: utf-8 -*-
"""
FILENAME.py , Built on Spyder for Python 2.7
James Watson, YYYY MONTHNAME
A ONE LINE DESCRIPTION OF THE FILE

"""
# == Init Environment ==

# ~ PATH Changes ~ 
def localize():
    """ Add the current directory to Python path if it is not already there """
    from sys import path # I know it is bad style to load modules in function
    import os.path as os_path
    containerDir = os_path.dirname(__file__)
    if containerDir not in path:
        path.append( containerDir )

localize() # You can now load local modules!

# ~ Standard Libraries ~
import math
from math import sqrt, ceil, sin, cos, tan, atan2
# ~ Special Libraries ~
import matplotlib.pyplot as plt
import numpy as np
# ~ Constants ~
EPSILON = 1e-7

# ~ Helper Functions ~

def eq(op1, op2):
    """ Return true if op1 and op2 are close enough """
    return abs(op1 - op2) <= EPSILON

# == End Init ==

def add_recursive(*args):
    print "There are ", str(len(args)), " args"
    if len(args) > 2:
        print "Entered the recursive branch"
        return args[0] + add_recursive(*args[1:]) # Note the star operator is needed for recursive call
        #                                           The star operator unpacks the list into positional arguments
    else:
        print "Entered the base case branch"
        return args[0] + args[1]
        
print add_recursive(1,2,3,4,5,6,7)

def require_two_args(arg1, arg2, *moreArgs):
    temp = arg1 + arg2
    for arg in moreArgs:
        temp += arg
    return temp

print require_two_args(1,2,3) # 6
print require_two_args(1,2)   # 3 , the above handles the missing optional args list gracefully