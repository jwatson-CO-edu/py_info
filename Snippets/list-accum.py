def accum_list( numList ):
    """ Return a list for which each element is a running total of the corresponding in 'pList' and all previous """
    accum = 0
    rtnList = []
    for num in numList:
        accum += num
        rtnList.append( accum )
    return rtnList

print [1,2,3,4,5]
print accum_list( [1,2,3,4,5] )