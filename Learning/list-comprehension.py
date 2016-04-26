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