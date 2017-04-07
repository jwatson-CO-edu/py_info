#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
RESULT: Swapped corresponding sections in two lists of equal length
"""

from random import randrange

ones = [ 1 for one in xrange( 30 ) ]
twos = [ 2 for two in xrange( 30 ) ]

for i in xrange( 10 ):
    # NOTE: This assumes that each list has at least 2 elements
    cut1 = randrange( len( ones ) - 1 ) 
    cut2 = randrange( cut1 + 1 , len( ones ) )
    print cut1 , cut2
    Alist = ones[ : cut1 ] + twos[ cut1 : cut2 ] + ones[ cut2 : ]
    Blist = twos[ : cut1 ] + ones[ cut1 : cut2 ] + twos[ cut2 : ]
    print Alist , len( Alist )
    print Blist , len( Blist )