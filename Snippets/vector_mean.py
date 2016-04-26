# -*- coding: utf-8 -*-

def vector_mean(*args): # This does the same thing as np.mean!
    rtnVec = []
    for index in xrange(len(args[0])): # assumes that all args are vectors of the same length
        rtnVec.append( 0 )
        for arg in args:
            rtnVec[index] += arg[index]
        rtnVec[index] /= len(args[0])
    return rtnVec