# Sort two lists in tandem, with one list as the 'keys' to sort by , URL: http://stackoverflow.com/a/6618543/893511

valList = [  0  ,  1  ,  2  ,  3  ,  4  ,  5  ,  6  ,  7  ,  8  ,  9  ]
keyList = [ 'q' , 'w' , 'e' , 'r' , 't' , 'y' , 'u' , 'i' , 'o' , 'p' ]

print sorted( keyList )
print [ val for ( key , val ) in sorted( zip( keyList , valList ) , key = lambda pair: pair[0] ) ]

def tandem_sort( keyList , valList ): # URL: http://stackoverflow.com/a/6618543/893511
    """ Sort two lists of equal length in tandem , with the elements of 'valList' reordered to correspond with a sorted 'keyList' , return copies """
    keySorted = sorted( keyList )
    valSorted = [ val for ( key , val ) in sorted( zip( keyList , valList ) , key = lambda pair: pair[0] ) ]
    return keySorted , valSorted

keySorted , valSorted = tandem_sort( keyList , valList )
print keySorted
print valSorted

def assoc_sort_tuples( keyList , valList ):
    """ Associate each element of 'keyList' with each element of 'valList' , sort on 'keyList' , return list of tuples """
    return [ elem for elem in sorted( zip( keyList , valList ) , key = lambda pair: pair[0] ) ]

print assoc_sort_tuples( keyList , valList )