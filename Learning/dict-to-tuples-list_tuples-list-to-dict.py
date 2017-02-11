# Serialize a dictionary into a list of ( key , val ) tuples
fooDict = { 'a':1 , 'b':2 , 'c':3 }
fooTuplesList = fooDict.items() 
print fooDict #                        {'a': 1, 'c': 3, 'b': 2}
print fooTuplesList #                  [('a', 1), ('c', 3), ('b', 2)]
print dict( fooTuplesList ) #          {'a': 1, 'c': 3, 'b': 2} # Turn the tuples back into a dictionary
print dict( tuple( fooTuplesList ) ) # {'a': 1, 'c': 3, 'b': 2} # Turn the tuples back into a dictionary
print {}.items() #                     []