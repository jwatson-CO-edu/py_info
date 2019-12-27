# Wrap angles in radians to [-pi,+pi]
import numpy as np
from numpy import pi

def angle_normPI( angle ):
    """ Wrap angles in radians to (-pi,+pi] """
    if angle == -pi:
        return pi
    nAngle = angle % (2*pi)
    if nAngle > pi:
        return nAngle - 2*pi
    return nAngle

def add_angle_normPI( ang1 , ang2 ):
    """ Wrap the sum of two angles in radians to (-pi,+pi] """
    return angle_normPI( ang1 + ang2 )

def subtract_angle_normPI( ang1 , ang2 ):
    """ Return the difference of two angles that wrap at -pi == +pi """
    angle1 = angle_normPI( ang1 )
    angle2 = angle_normPI( ang2 )
    if angle1 >= 0.0:
        if angle2 >= 0.0:
            return angle1 - angle2
        else:
            return - ( pi + angle2 ) - ( pi - angle1 )
    else:
        if angle2 >= 0.0:
            return + ( pi - angle2 ) + ( pi + angle1 )
        else:
            return angle1 - angle2
        

