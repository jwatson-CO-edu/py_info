#!/usr/bin/env python

def same_contents_list( lst1 , lst2 ):
    s1 = set( lst1 ) ; s2 = set( lst2 )
    return s1 == s2

print same_contents_list( [1,2,3] , [3,2,1] ) # True
print same_contents_list( [1,2,3] , [3,2] ) #   False
print same_contents_list( [1,2,3] , [3,2,4] ) # False