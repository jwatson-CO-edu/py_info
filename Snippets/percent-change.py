from __future__ import division

def percent_change( oldVal , newVal ):
    """ Return the precent change from 'oldVal' to 'newVal' """
    return ( newVal - oldVal ) / oldVal * 100.0

print percent_change( 5 , 7 )
print percent_change( 7 , 5 )
print percent_change( 1 , 0 )
# print percent_change( 0 , 1 ) # Divide by 0 
print percent_change( 1e309 , 1 ) # nan