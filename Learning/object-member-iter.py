#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Template Version: 2017-04-13

# ~~ Future First ~~
from __future__ import division # Future imports must be called before everything else, including triple-quote docs!

"""
RESULT: 
"""

class Foo:
    def __init__( self ):
        self.a = 1
        self.b = 2
        
class Bar(object):
    def __init__( self ):
        self.a = 1
        self.b = 2
        
baz = Foo()
qux = Bar()

# 1. Try to iterate over a Foo and see what happens
#for elem in bar: # ERROR
    #print elem
    
# 2. Try to iterate over a bar and see what happens
for elem in qux: # ERROR
    print elem