# -*- coding: utf-8 -*-

print "== Built In Types =="
print isinstance([1,2,3], list) # ------- True,  a list
print isinstance((1,2,3), list) # ------- False, iterable but not list
print isinstance("foo", list) # --------- False, iterable but not list
print isinstance((1,2,3), (list,tuple)) # True,  tuple is one of list or tuple
print isinstance([1,2,3], (list,tuple)) # True,  list is one of list or tuple

import collections

print "== Iterable =="
print isinstance( (1,2,3) , collections.Iterable ) # True
print isinstance( [1,2,3] , collections.Iterable ) # True

print "== Hashable =="
print isinstance( (1,2,3) , collections.Hashable ) # True
print isinstance( [1,2,3] , collections.Hashable ) # False

import numpy as np

print "== Python and Numpy Arrays =="
print isinstance([] , (list,np.ndarray)) #                      True
print isinstance(np.array([0.0,0.0,0.0]) , (list,np.ndarray)) # True
print np.any( [ 0.0 , 0.0 , 0.0 ] ) #                            False , This is not an appropriate test if an array is not None

print "== Classes =="
print (3).__class__.__name__ == 'int' # True
class foo(): pass
bar = foo()
print bar.__class__.__name__ == 'foo' # True
print bar.__class__ == foo #            True

print "== Class and Superclass =="
class baz(foo): pass
qux = baz()
print isinstance( qux , foo ) #         True , Superclasses count!
print isinstance( qux , baz ) #         True
print qux.__class__ == foo #            False
print qux.__class__ == baz #            True
print qux.__class__.__name__ == 'foo' # False
print qux.__class__.__name__ == 'baz' # True