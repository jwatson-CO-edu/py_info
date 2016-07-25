def lists_as_columns_with_titles(titles, lists):
    """ Print each of the 'lists' as columns with the appropriate 'titles' """
    longestList = 0
    longestItem = 0
    prntLists = []
    pad = 4 * ' '
    if len(titles) == len(lists):
        for lst in lists:
            if len(lst) > longestList:
                longestList = len(lst)
            prntLists.append( [] )
            for item in lst:
                strItem = str(item)
                prntLists[-1].append( strItem )
                if len(strItem) > longestItem:
                    longestItem = len(strItem)
        line = ''
        for title in titles:
            line += title[ : len(pad) + longestItem -1 ].rjust( len(pad) + longestItem , ' ' )
        print line
        for index in range(longestList):
            line = ''
            for lst in prntLists:
                if index < len(lst):
                    line += pad + lst[index].ljust(longestItem, ' ')
                else:
                    line += pad + longestItem * ' '
            print line
    else:
        print "Titles" , len(titles) , "and lists" , len(lists) , "of unequal length"
        
lists_as_columns_with_titles(['foo','bar','baz'], [[1,2,3],[4,5,6,7],[8,9]])
"""
  foo  bar  baz
    1    4    8
    2    5    9
    3    6     
         7     
"""