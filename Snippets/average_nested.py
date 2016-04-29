# -*- coding: utf-8 -*-

def avg(*args):
    """ Average of args, where args can be a list or nested lists """
    total, N = accumulate(args)
    return float(total) / N
    
def accumulate(pLst):
    """ Return the sum of all items in 'pLst'. Return the total number of non-list/tuple items in 'pLst'. Recursive """
    total = 0
    N = 0
    for item in pLst:
        if isinstance(item, (list,tuple)):
            partTot, partN = accumulate(item)
            total += partTot
            N += partN
        else:
            total += item
            N += 1
    return total, N
    
print avg([1,2,3,4,5]) #       3.0
print avg(1,2,3,4,5) #         3.0
print avg(1,[2,[3,[4,[5]]]]) # 3.0