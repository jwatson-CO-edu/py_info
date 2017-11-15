from math import sqrt
import numpy as np

def d_point_to_segment_2D_signed( point , segment ): 
    """ Return the signed ( + RHS , - LHS ) perpendicular distance between 'point' and a line 'segment' defined from tail to head """
    # URL: http://mathworld.wolfram.com/Point-LineDistance2-Dimensional.html
    segPt1 = segment[0] ; segPt2 = segment[1]
    num = ( segPt2[0] - segPt1[0] ) * ( segPt1[1] - point[1] ) - ( segPt1[0] - point[0] ) * ( segPt2[1] - segPt1[1] )
    return abs( num ) / sqrt( ( segPt2[0] - segPt1[0] )**2 + ( segPt2[1] - segPt1[1] )**2 ) * np.sign( num )

segmentUp = ( ( 0 , 0 ) , ( 0 , 4 ) )
segmentDn = ( ( 0 , 4 ) , ( 0 , 0 ) )
pntLeft   = ( -2 ,  0 )
pntRght   = (  2 ,  0 )

print "Segment UP   , Point LEFT :" , d_point_to_segment_2D_signed( pntLeft , segmentUp )
print "Segment UP   , Point RIGHT:" , d_point_to_segment_2D_signed( pntRght , segmentUp )
print "Segment DOWN , Point LEFT :" , d_point_to_segment_2D_signed( pntLeft , segmentDn )
print "Segment DOWN , Point RIGHT:" , d_point_to_segment_2D_signed( pntRght , segmentDn )
print d_point_to_segment_2D_signed( (150.0, 90.0) , ((0.0, 0.0), (300.0, 0.0)) )
