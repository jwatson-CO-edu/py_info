# Sort two lists in tandem, with one list as the 'keys' to sort by , URL: http://stackoverflow.com/a/6618543/893511

valList = [  0  ,  1  ,  2  ,  3  ,  4  ,  5  ,  6  ,  7  ,  8  ,  9  ]
otherLs = [ 10  , 11  , 12  , 13  , 14  , 15  , 16  , 17  , 18  , 19  ]
lastLst = [ 20  , 21  , 22  , 23  , 24  , 25  , 26  , 27  , 28  , 29  ]
keyList = [ 'q' , 'w' , 'e' , 'r' , 't' , 'y' , 'u' , 'i' , 'o' , 'p' ]

print sorted( keyList )
print [ val for ( key , val ) in sorted( zip( keyList , valList ) , key = lambda pair: pair[0] ) ]

def tandem_sort( keyList , *otherLists ):
    """ Sort multiple lists of equal length in tandem , with the elements of each in 'otherLists' reordered to correspond with a sorted 'keyList' """
    # keySorted = sorted( keyList )
    bundle = sorted( zip( keyList , *otherLists ) , key = lambda elem: elem[0] ) # Sort the tuples by the key element
    rtnLists = [ [] for i in xrange( len( bundle[0] ) ) ]
    for elemTuple in bundle:
        for index , elem in enumerate( elemTuple ):
            rtnLists[ index ].append( elem ) # Send the element to the appropriate list
    return rtnLists
            

[ keySorted , valSorted ] = tandem_sort( keyList , valList ) # You can unpack a list return into named list components!
print keySorted
print valSorted
# We can sort as many lists as we want to!
[ keySort , valSort , othSort , lasSort ] = tandem_sort( keyList , valList , otherLs , lastLst )

for sortList in [ keySort , valSort , othSort , lasSort ]:
    print sortList

class SortedMembers:
    """ A silly class to test whether 'tandem_sort' can be used to sort multiple member functions , in place """
    
    def __init__( self ):
        """ Some lists that will be reordered according to the keylist """
        self.valList = [  0  ,  1  ,  2  ,  3  ,  4  ,  5  ,  6  ,  7  ,  8  ,  9  ]
        self.otherLs = [ 10  , 11  , 12  , 13  , 14  , 15  , 16  , 17  , 18  , 19  ]
        self.lastLst = [ 20  , 21  , 22  , 23  , 24  , 25  , 26  , 27  , 28  , 29  ]
        self.keyList = [ 'q' , 'w' , 'e' , 'r' , 't' , 'y' , 'u' , 'i' , 'o' , 'p' ]
        
    def sort_own_members( self ):
        """ Attempt to sort all member lists in place """ # THIS WORKS
        [ self.keyList , self.valList , self.otherLs , self.lastLst ] = tandem_sort( self.keyList , self.valList , self.otherLs , self.lastLst )

foo = SortedMembers()
print "Try Sorting Member Lists"
foo.sort_own_members()
for sList in [ foo.keyList , foo.valList , foo.otherLs , foo.lastLst ]:
    print sList

def assoc_sort_tuples( keyList , valList ):
    """ Associate each element of 'keyList' with each element of 'valList' , sort on 'keyList' , return list of tuples """
    return [ elem for elem in sorted( zip( keyList , valList ) , key = lambda pair: pair[0] ) ]

print assoc_sort_tuples( keyList , valList )