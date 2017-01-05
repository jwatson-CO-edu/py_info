""" Remove an object from a list of objects by a reference to the object """

class Thing:
    def __init__( self , num ):
        self.num = num
        
thingList = [ Thing(i) for i in xrange( 10 ) ]
print thingList
print [ item.num for item in thingList ]
ref = thingList[4]
print thingList.remove( ref )
print [ item.num for item in thingList ]