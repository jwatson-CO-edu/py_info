# -*- coding: utf-8 -*-
class Foo(object):
    """ dummy class """
    pass

bar = []
baz = []

for i in range(3):
    bar.append( Foo()  )
    baz.append( bar[i] )
    
for i in range(3):
    print "Objects are the same:  ", bar[i] is baz[i]
    print "Objects are equivalent:", bar[i] == baz[i]
    print "Addresses:", bar[i] ,  baz[i]