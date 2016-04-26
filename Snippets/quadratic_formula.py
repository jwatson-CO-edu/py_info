""" Find the roots of a quadratic (2nd Order) polynomial
To the tune of "Pop Goes the Weasel":
x equals the opposite of b, 
plus or minus the square root, 
of b squared minus 4 a c, 
all over 2 a """

import math

def quad(a,b,c):
    roots = []
    d = b ** 2 - 4 * a * c
    if d > 0:
        roots.append( (-1 * b + math.sqrt(d))/ (2 * a) )
        roots.append( (-1 * b - math.sqrt(d))/ (2 * a) )
    elif d == 0:
        roots.append( (-1 * b) / (2 * a ) )
    else:
        real = (-1 * b) / ( 2 * a )
        im = math.sqrt(abs(d)) / (2 * a)
        roots.append( str( real ) + ' + ' + str( im ) + 'j' )
        roots.append( str( real ) + ' - ' + str( im ) + 'j' )
    for root in roots:
        print( str( root ) + '\n' )
    return roots