# -*- coding: utf-8 -*-
print isinstance([1,2,3], list) # ------- True,  a list
print isinstance((1,2,3), list) # ------- False, iterable but not list
print isinstance("foo", list) # --------- False, iterable but not list
print isinstance((1,2,3), (list,tuple)) # True,  tuple is one of list or tuple
print isinstance([1,2,3], (list,tuple)) # True,  list is one of list or tuple