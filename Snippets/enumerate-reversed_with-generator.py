# Non-generator option
for i, e in reversed(list(enumerate(['a','b','c']))):
    print i, e
"""
2 c
1 b
0 a
"""
    
print '\n',list(enumerate(['a','b','c'])),'\n' # [(0, 'a'), (1, 'b'), (2, 'c')]
# Calling 'list' on 'enumerate' creates a list of index-value tuples!

# Generator option
def enumerate_reverse(L):
    """ A generator that works like 'enumerate' but in reverse order """
    # URL, Generator that is the reverse of 'enumerate': http://stackoverflow.com/a/529466/893511
    for index in reversed(xrange(len(L))):
        yield index, L[index]
        
for i, e in enumerate_reverse(['a','b','c']):
    print i, e
"""
2 c
1 b
0 a
"""