#!/usr/bin/env python
# -*- coding: utf-8 -*-

def elemw(i, iterable):
    """ Return the 'i'th index of 'iterable', wrapping to index 0 at all integer multiples of 'len(iterable)' """
    return iterable[ i % ( len(iterable) ) ]
                    
def elem_surrounding( i , margin , wList ):
    rtnList = [ elemw( index , wList ) for index in xrange( i-margin , i+1 ) ]
    rtnList.extend( [ elemw( index , wList ) for index in xrange( i+1 , i+margin+1  ) ] )
    return rtnList
    
foo = [0,1,2,3,4]
print elemw(2 , foo) # 2
print elemw(5 , foo) # 0
print elem_surrounding( 4 , 2 , foo )
