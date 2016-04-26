# -*- coding: utf-8 -*-
""" Multiple variables can be populated in a list comprehension """
for a, b, c, d in [[1,2,3,4],
                   ['A','B','C','D'],
                   [[1,2,3,4],[4,3,2,1],[5,6,7,8],[8,7,6,5]]]:
                       
    print "a:",a,"\tb:",b,"\tc:",c,"\td:",d
    
foo = [[x[0],x[1],x[0]+x[1]] for x in [[1,1],[2,2],[3,3]]]
print foo # [[1, 1, 2], [2, 2, 4], [3, 3, 6]]

import random
# slots = [[]] * 200 # This creates 200 references to the same list! The result will be that each of the cells in slots
#will be a reference to the same list! # URL, shallow copy with '*': http://stackoverflow.com/a/240205/893511
# This is not normally a problem when the 'x' in '[x] * INT' is a mutable type.  However, when mutable types are involved,
#the idiom below is to be used if separate nested lists are to be produced
slots = [[] for i in range(200)]

for i in range(4000):
    index = random.randrange(200)
    slots[index].append( random.randrange(5) )
    
print slots[0] == slots[100] == slots[199] 