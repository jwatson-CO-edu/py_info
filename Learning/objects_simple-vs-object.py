#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Template Version: 2017-04-13

# ~~ Future First ~~
from __future__ import division # Future imports must be called before everything else, including triple-quote docs!

"""
RESULT: Inheriting 'object' comes with default implementations of many __dunderscore__ functions versus a bare object with no parent class 
        specified, which in contrast has very few of these. 
        
        Bare objects might come in handy for simple container classes and other lightweight implementations that are never expected to be
        printed or otherwise provide boilerplate info

bare:   ['__doc__', '__init__', '__module__']
object: ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', 
         '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
"""

# The definition of the '__init__' function of these two classes is identical , however Bar inherits many members from 'object'

class Foo:
    def __init__( self , inVar ):
        self.myVar = inVar
        
class Bar( object ):
    def __init__( self , inVar ):
        self.myVar = inVar
        
baz = Foo( 1 )
xur = Bar( 2 )
print "Foo:" , dir( baz )
print "Bar:" , dir( xur )

"""
Foo: ['__doc__', '__init__', '__module__', 'myVar']
Bar: ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', 
      '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
      'myVar']
"""