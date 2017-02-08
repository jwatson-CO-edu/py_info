import os
# ~~ Constants , Shortcuts , Aliases ~~
import __builtin__ # URL, add global vars across modules: http://stackoverflow.com/a/15959638/893511
__builtin__.EPSILON = 1e-7
__builtin__.infty = 1e309 # URL: http://stackoverflow.com/questions/1628026/python-infinity-any-caveats#comment31860436_1628026
__builtin__.endl = os.linesep

def eq_margin( op1 , op2 , margin = EPSILON ): # >>> resenv
    """ Return true if op1 and op2 are within 'margin' of each other, where 'margin' is a positive real number """
    return abs( op1 - op2 ) <= margin

def equality_test_w_margin( margin = EPSILON ):
    """ Return a function that performs an 'eq' comparison with the specified margin """
    def eq_test( op1 , op2 ):
        return eq_margin( op1 , op2 , margin )
    return eq_test

def list_search_w_test( pList , item , eqTest ):
    """ Linear search of 'pList' , determine membership with 'eqTest' and return index if the test passes , Otherwise return None if DNE """
    for i , elem in enumerate( pList ):
        if eqTest( item , elem ):
            return i
    return None

exList = range(6)
print exList
print list_search_w_test( exList , 3.1 , equality_test_w_margin( 0.5 ) ) # 3
print list_search_w_test( exList , 7.0 , equality_test_w_margin( 0.5 ) ) # None
