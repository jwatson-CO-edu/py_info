def nth_index_of_in( n , item , seq ): 
    """ Return the index of the 'n'th instance of 'item' in the sequence , Return -1 if there are not 'n' occurrences """
    startDex = 0
    for i in xrange(n):
        startDex = seq.find( item , startDex ) + 1
    return startDex - 1

print nth_index_of_in( 4  , 'dog' , 'dogcatdogcatdogdogdogdogdogdogdog' ) # 15
print nth_index_of_in( 40 , 'dog' , 'dogcatdogcatdogdogdogdogdogdogdog' ) # -1