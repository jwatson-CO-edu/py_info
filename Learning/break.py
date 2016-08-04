# -*- coding: utf-8 -*-
for i in xrange(4000):
    print i, 
    if i > 5:
        break
# "0 1 2 3 4 5 6"

import random

for i in range(10):
    for j in range(10):
        num = random.randrange(1,11)
        print i , "," , j , ":" , num
        if num > 5:
            print "break"
            break
"""
0 , 0 : 5
0 , 1 : 5
0 , 2 : 6
break <---- Only breaks from the innermost loop!
1 , 0 : 10
break
2 , 0 : 10
"""
print
broken = False
for i in range(10):
    if broken:
        break
    for j in range(10):
        num = random.randrange(1,11)
        print i , "," , j , ":" , num
        if num > 5:
            print "break"
            broken = True
            break
"""
0 , 0 : 4
0 , 1 : 1
0 , 2 : 8
break <--- Breaks all the way out!
"""