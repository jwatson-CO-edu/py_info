#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Template Version: 2017-04-13

# ~~ Future First ~~
from __future__ import division # Future imports must be called before everything else, including triple-quote docs!

"""
RESULT: A function that returns multiple values can unpack into a tuple , and that tuple assigned to a variable in the same statement
"""

def rtn_two_vars():
    """ Return two numbers """
    return 1 , 2

testTpl = ( var1 , var2 ) = rtn_two_vars()

print "var1:   " , var1
print "var2:   " , var2
print "testTpl:" , testTpl

"""
var1:    1
var2:    2
testTpl: (1, 2)
"""