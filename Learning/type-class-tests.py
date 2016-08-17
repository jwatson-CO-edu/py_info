import numpy as np

print isinstance([] , (list,np.ndarray)) #                      True
print isinstance(np.array([0.0,0.0,0.0]) , (list,np.ndarray)) # True
print np.any([0.0,0.0,0.0]) #                                   False , This is not an appropriate test if an array is not None

print (3).__class__.__name__ == 'int' # True
class foo(): pass
bar = foo()
print bar.__class__.__name__ == 'foo' # True
print bar.__class__ == foo #            True