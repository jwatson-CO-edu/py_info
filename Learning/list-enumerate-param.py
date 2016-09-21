foo = ['q','w','e','r','t','y','u','i']
print foo

for i , ltr in enumerate(foo , -1):
    print i,ltr
"""
-1 q
 0 w
 1 e
 2 r
 3 t
 4 y
 5 u
 6 i
"""

print

for i , ltr in enumerate(foo[2:]):
    print i,ltr
"""
0 e
1 r
2 t
3 y
4 u
5 i
"""
