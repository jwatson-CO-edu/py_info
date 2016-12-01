class Thing:
    def __init__( self , num ):
        self.num = num

def find_pop( iterable , item ):
    """ Pop 'item' from 'iterable' , ValueError if not in 'iterable' """
    return iterable.pop( iterable.index( item ) )
        
thingList = [ Thing(i) for i in xrange( 10 ) ]
print [ item.num for item in thingList ]
ref = thingList[4]
print "Found and popped" , find_pop( thingList , ref ).num
print [ item.num for item in thingList ]

"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Found and popped 4
[0, 1, 2, 3, 5, 6, 7, 8, 9]
"""