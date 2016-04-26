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
    
def sep(title = ""):
    """ Print a separating title card for printing """
    LINE = '======'
    print LINE + ' ' + title + ' ' + LINE

# == End Init ==

def bbClass_init(cls, pBar, pBaz):
    """ Used to init 'Foo' and its subclasses """
    cls.bar = pBar
    cls.baz = pBaz

class Foo(object):
    bar = 0
    baz = 'a'
    
    @staticmethod
    def incr_class_bar():
        # bar += 1 # ERROR : No access to class vars here!
        pass
    
    def init_class(self, pBaz = None): # I wanted to avoid having to instantiate a class first
        self.__class__.bar = 0
        self.__class__.baz = pBaz
        
class Qux(Foo):
    # The class variables 'bar' and 'baz' were inherited, along with their values, even though no object was 
    #instantiated from either
    pass

bbClass_init(Foo, 1, 'Foo')
bbClass_init(Qux, 2, 'Qux')

sep('Foo')
print Foo.bar
print Foo.baz
sep('Qux')
print Qux.bar
print Qux.baz