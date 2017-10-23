#!/usr/bin/env python
"""
RESULT: If the elements in a list are themselves iterables , you can decompose the nested elements with the pattern: 
        'for [ subElem1 , subElem2 ] in superList' 
        for a list that takes the form 
        superList = [ ... , [ i1 , i2 ] , ...  ]
"""

from random import randint

listList = []
N = 10

for i in xrange( N ):
    listList.append( [ randint( 1 , 5 ) , randint( 6 , 10 ) ] )
    
for [ op1 , op2 ] in listList:
    print "Decomposed pair:" , op1 , "and" , op2