# -*- coding: utf-8 -*-

foo = [None] * 4
print foo # [None, None, None, None]

i = 0
for item in foo:
    i += 1
    item = i
print foo # [None, None, None, None] # did not modify via 'item'!

for i in xrange(4):
    foo[i] = i
print foo # [0, 1, 2, 3] # able to modify via the index

# 'enumerate' is quite handy for times when you want to work with both the items of a list and their indices
for i, item in enumerate(['a','b','c']):
    print i, item
# 0 a
# 1 b
# 2 c

bar = range(51)
print [item for item in bar if item%2==0] # build a list that is only the even numbers
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

# Reversing tuples and lists
foo = [1,2,3]
bar = (1,2,3)
baz = foo[::-1] # Reverse a list
qux = bar[::-1] # Reverse a tuple
print foo
print bar
print baz
print qux