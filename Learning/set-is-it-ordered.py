from random import randrange

foo = set( [ randrange( 5000 ) for rNum in xrange( 500 ) ] )
bar = tuple( foo )

diffCount = 0
for i in xrange( 1000 ):
    if tuple( set( bar ) ) != bar:
        diffCount += 1
        
print "The tuplation of a set of a tuple was different on" , diffCount , "occasions."
#      The tuplation of a set of a tuple was different on 1000 occasions.