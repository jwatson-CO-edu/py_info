# Test conditional skipping in a 'for' loop

for i in xrange( 40 ):
    if (i % 4 == 0) and (i > 0):
        continue # immediately shortcuts past the rest of the block and proceeds directly to the next loop
    print i ,
# 0 1 2 3 5 6 7 9 10 11 13 14 15 17 18 19 21 22 23 25 26 27 29 30 31 33 34 35 37 38 39
print
for i in xrange( 41 ):
    if i % 4 == 0:
        print "Skipping" , i , "|" ,
        continue
    if i % 2 == 0:
        print i , "is even" , "|" ,
print
for i in xrange( 41 ):
    if i % 4 == 0:
        print "Skipping" , i , "|" ,
        next # DOES NOTHING , 'next()' is used in the context of iterators , not loops
    if i % 2 == 0:
        print i , "is even" , "|" ,
"""
Skipping 0 | 2 is even | Skipping 4 | 6 is even | Skipping 8 | 10 is even | Skipping 12 | 14 is even | Skipping 16 | 18 is even | Skipping 20 | 22 is even | Skipping 24 | 26 is even | Skipping 28 | 30 is even | Skipping 32 | 34 is even | Skipping 36 | 38 is even | Skipping 40 |
Skipping 0 | 0 is even | 2 is even | Skipping 4 | 4 is even | 6 is even | Skipping 8 | 8 is even | 10 is even | Skipping 12 | 12 is even | 14 is even | Skipping 16 | 16 is even | 18 is even | Skipping 20 | 20 is even | 22 is even | Skipping 24 | 24 is even | 26 is even | Skipping 28 | 28 is even | 30 is even | Skipping 32 | 32 is even | 34 is even | Skipping 36 | 36 is even | 38 is even | Skipping 40 | 40 is even |
"""
