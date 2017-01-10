def insert_sublist( bigList , index , subList ):
    """ Insert 'subList' into 'bigList' at 'index' and return resulting list """
    return bigList[:index] + subList + bigList[index:]

def replace_sublist( bigList , begDex , endDex , subList ):
    """ Replace the elements in 'bigList' from 'begDex' to 'endDex' with 'subList' """
    return bigList[:begDex] + subList + bigList[endDex:]

print insert_sublist( [1,2,3,4] , 2 , ['a','b','c'] ) #      [1, 2, 'a', 'b', 'c', 3, 4]
print replace_sublist( [1,2,3,4] , 1 , 3 , ['a','b','c'] ) # [1, 'a', 'b', 'c', 4]