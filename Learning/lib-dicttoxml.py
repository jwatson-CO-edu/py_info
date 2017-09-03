#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Template Version: 2017-04-13

# ~~ Future First ~~
from __future__ import division # Future imports must be called before everything else, including triple-quote docs!

from dicttoxml import dicttoxml

"""
RESULT: A dictionary is serialized into an XML string , 'dicttoxml' automatically adds a header whenever a custom root is specified , but 
        this is manageable with the function provided
"""

def remove_XML_header( pString ):
    """ Remove the XML header from 'pString' """
    skipping = True
    skipStop = '>'
    rtnStr = ""
    for char in pString:
        if not skipping:
            rtnStr += char        
        if char == skipStop:
            skipping = False
    return rtnStr
        

foo = dicttoxml( { 'a':1 , 'b':2 , 'c':3 } , custom_root = 'record' )
rtnStr = ""
for i in xrange( 3 ):
    rtnStr += remove_XML_header( foo ) + '\n'
print foo
print rtnStr