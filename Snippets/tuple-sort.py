def sort_tuple( tup ):
    """ Return a sorted copy of 'tup' """
    return tuple( sorted( list( tup ) ) )

print sort_tuple( ('zzz','dog','cat') ) # ('cat', 'dog', 'zzz') # The copy tuple is alphabetized
print sort_tuple( (20,100,5) ) #          (5, 20, 100)