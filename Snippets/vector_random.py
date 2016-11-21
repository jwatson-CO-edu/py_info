from random import random

def vec_random( dim ): # <<< resenv
    """ Return a random vector in R-'dim' space with coordinates in [0,1) """
    rtnVec = []
    for i in range(dim):
        rtnVec.append( random() )
    return rtnVec

def vec_random_limits( dim , limits ):
    """ Return a vector in which each element takes on a random value between 'limits[i][0]' and 'limits[i][1]' with a uniform distribution """
    rtnVec = []
    randVec = vec_random( dim )
    for i , elem in enumerate( randVec ):
        span = abs( limits[i][1] - limits[i][0] )
        rtnVec.append( elem * span + limits[i][0] )
    return rtnVec