import numpy as np

class ArrayContainer(object):

    def __init__(self,q_1, q_2, q_3):
        """ Return a quaternion specified by the scalar part followed by the components of the vector part """
        self._vctr = np.array( [ q_1 , q_2 , q_3 ] )
        
    @property
    def vctr(self):
        return self._vctr.copy() # Note that if you name the var 'vctr' then 'vctr' will be called, resulting in infinite loop
    
    @vctr.setter
    def vctr(self, arr_or_list):
        self._vctr = np.array( arr_or_list )

foo = ArrayContainer( 1,2,3 )

print foo.vctr # [1 2 3]
foo.vctr = [4,5,6]
print foo.vctr # [4 5 6] # Behaves as expected