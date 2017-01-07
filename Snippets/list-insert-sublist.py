def insert_sublist( bigList , index , subList ):
    """ Insert 'subList' into 'bigList' at 'index' and return resulting list """
    return bigList[:index] + subList + bigList[index:]

print insert_sublist( [1,2,3,4] , 2 , ['a','b','c'] ) # [1, 2, 'a', 'b', 'c', 3, 4]