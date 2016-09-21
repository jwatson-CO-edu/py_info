from __future__ import division
import numpy as np
from math import trunc

def incr_min_step( bgn , end , stepSize ):
    """ Return a list of numbers from 'bgn' to 'end' (inclusive), separated by at LEAST 'stepSize'  """
    # NOTE: The actual step size will be the size that produces an evenly-spaced list of trunc( (end - bgn) / stepSize ) elements
    return np.linspace( bgn , end , num = trunc( (end - bgn) / stepSize ) , endpoint=True )

def incr_max_step( bgn , end , stepSize ):
    """ Return a list of numbers from 'bgn' to 'end' (inclusive), separated by at MOST 'stepSize'  """
    numSteps = (end - bgn) / stepSize
    rtnLst = [ bgn + i * stepSize for i in xrange( trunc(numSteps) + 1 ) ]
    if numSteps % 1 > 0:
        rtnLst.append( end )
    return rtnLst
    
print incr_min_step( 0 , 10 ,  1.5 ) # [  0.   2.   4.   6.   8.  10.]
print incr_max_step( 0 , 10 ,  1.5 ) # [0.0, 1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10]
print incr_max_step( 0 ,  6 ,  1.5 ) # [0.0, 1.5, 3.0, 4.5, 6.0]
print incr_min_step( 2 ,  5 , 10 )   # []
print incr_max_step( 2 ,  5 , 10 )   # [2,   5]