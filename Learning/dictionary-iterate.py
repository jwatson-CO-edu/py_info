# -*- coding: utf-8 -*-
def sep(title = ""):
    """ Print a separating title card for printing """
    LINE = '======'
    print LINE + ' ' + title + ' ' + LINE

testLookup = {'foo':1,'bar':2,'baz':3}

sep('Simple for')
for key in testLookup:
    print key, testLookup[key]

sep('Dictionary Iterator')
for item, key in testLookup.iteritems(): # Note that 'items' will return a COPY of all key value pairs!
    # 'iteritems' is preferred for Python 2.N. In Python 3 it is removed, but 'items' has the 'iteritems' behavior
    print item, key
    
#baz 3
#foo 1
#bar 2
    
sep('Deleting Keys')
testLookup.clear()
for item, key in testLookup.iteritems(): # Note that 'items' will return a COPY of all key value pairs!
    print item, key # Nothing printed