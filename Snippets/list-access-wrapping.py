#!/usr/bin/env python
# -*- coding: utf-8 -*-

def elemw(iterable, i):
    """ Return the 'i'th index of 'iterable', wrapping to index 0 at all integer multiples of 'len(iterable)' """
    return iterable[ i % ( len(iterable) ) ]
    
foo = [0,1,2,3,4]
print elemw(foo, 2) # 2
print elemw(foo, 5) # 0