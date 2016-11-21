def assoc_find_all( findList , assocList , key ):
    """ Return a sublist of 'assocList' associated with all the elements in 'findList' that match 'key' """
    return [ assocList[i] for i , x in enumerate( findList ) if x == key ]

def assoc_find_max( findList , assocList ):
    """ Return a sublist of 'assocList' associated with all the elements in 'findList' that match the maximum value of 'findList' """
    return assoc_find_all( findList , assocList , max( findList ) )

searchL = [  1 , 2 , 2 , 3 , 3  ]
assocLs = [ 'a','b','c','d','e' ]

print assoc_find_all( searchL , assocLs , 2 ) # ['b', 'c'] 
print assoc_find_max( searchL , assocLs ) #     ['d', 'e']