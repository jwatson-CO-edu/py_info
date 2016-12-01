foo = [ 0 , 1 , 2 , 3 , 4 , 5 ]
print foo
print "Popped" , foo.pop(2)
print foo
print "Popped" , foo.pop(2)
print foo

"""
[0, 1, 2, 3, 4, 5]
Popped 2
[0, 1, 3, 4, 5]
Popped 3
[0, 1, 4, 5]
"""