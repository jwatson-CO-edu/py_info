# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
== NOTES ==
2016-03-17: 'intersect_seg_2D' is the best of the bunch.  Use it to detect intersections of line segments
"""

def sep(title = ""):
    """ Print a separating title card for debug """
    LINE = '======'
    print LINE + ' ' + title + ' ' + LINE


class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def ccw(A,B,C):
	return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)

def intersect(A,B,C,D):
	return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


a = Point(0,0)
b = Point(0,1)
c = Point(1,1)
d = Point(1,0)

e = Point(0,0)
f = Point(2,0)
g = Point(1,0)
h = Point(3,0)

sep('intersect')
print intersect(a,b,c,d)
print intersect(a,c,b,d)
print intersect(a,d,b,c)
print intersect(e,f,g,h) # False # Does not detect segments with an overlapping portion!
print intersect(e,f,e,f) # False # Does not detect identical segments

# http://www-cs.ccny.cuny.edu/~wolberg/capstone/intersection/Intersection%20point%20of%20two%20lines.html

def intersect2(p1,p2,p3,p4):
    den =   (p4[1] - p3[1])*(p2[0] - p1[0]) - (p4[0] - p3[0])*(p2[1] - p1[1])
    uAnum = (p4[0] - p3[0])*(p1[1] - p3[1]) - (p4[1] - p3[1])*(p1[0] - p3[0])
    uBnum = (p2[0] - p1[0])*(p1[1] - p3[1]) - (p2[1] - p1[1])*(p1[0] - p3[0])
    if den == 0:
        if uAnum == 0 or uBnum == 0:
            return True
        else:
            return False
    else:
        uA = uAnum * 1.0 / den
        uB = uBnum * 1.0 / den
        if (uA >= 0 and uA <= 1) and (uB >= 0 and uB <= 1):
            return True
        else:
            return False
            
a = (0,0)
b = (0,1)
c = (1,1)
d = (1,0)

e = (0,0)
f = (2,0)
g = (1,0)
h = (3,0)

sep('intersect2')
print intersect2(a,b,c,d)
print intersect2(a,c,b,d)
print intersect2(a,d,b,c)
print intersect2(e,f,g,h) # True # Does detect segments with an overlapping portion!
print intersect2(e,f,e,f) # True # Does detect identical segments!




#def intersect3(p1,p2,p3,p4):
def intersect_seg_2D( seg1 , seg2 ): # seg1[0] seg1[1] seg2[0] seg2[1]
    """ Return true if line segments 'seg1' and 'seg2' intersect, otherwise false """
    # URL: http://www-cs.ccny.cuny.edu/~wolberg/capstone/intersection/Intersection%20point%20of%20two%20lines.html
    # NOTE: 'uA' and 'uB' could be used to calc intersection point if desired, see above URL
    den =   (seg2[1][1] - seg2[0][1])*(seg1[1][0] - seg1[0][0]) - (seg2[1][0] - seg2[0][0])*(seg1[1][1] - seg1[0][1])
    uAnum = (seg2[1][0] - seg2[0][0])*(seg1[0][1] - seg2[0][1]) - (seg2[1][1] - seg2[0][1])*(seg1[0][0] - seg2[0][0])
    uBnum = (seg1[1][0] - seg1[0][0])*(seg1[0][1] - seg2[0][1]) - (seg1[1][1] - seg1[0][1])*(seg1[0][0] - seg2[0][0])
    if den == 0:
        if uAnum == 0 or uBnum == 0:
            return True
        else:
            return False
    else:
        uA = uAnum * 1.0 / den
        uB = uBnum * 1.0 / den
        if (uA >= 0 and uA <= 1) and (uB >= 0 and uB <= 1):
            return True
        else:
            return False
            
sep('intersect_seg_2D')
print intersect_seg_2D((a,b),(c,d))
print intersect_seg_2D((a,c),(b,d))
print intersect_seg_2D((a,d),(b,c))
print intersect_seg_2D((e,f),(g,h)) # True # Does detect segments with an overlapping portion!
print intersect_seg_2D((e,f),(e,f)) # True # Does detect identical segments!
print intersect_seg_2D(([0,0],[0,2]),([0,1],[4,4])) # True
print intersect_seg_2D(([0,0],[0,2]),([4,4],[0,1])) # True
print intersect_seg_2D(([4,4],[0,1]),([0,0],[0,2])) # True
print intersect_seg_2D(([4,4],[0,1]),([0,2],[0,0])) # True