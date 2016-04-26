# -*- coding: utf-8 -*-

foo = lambda x, y: (x+y, x-y) # OK : lambda can return one value
#bar = lambda x, y: x+y, x-y  # ERROR : Cannot use multiple returns as you can with a def function, with lambda you must
#                                       pack multiple values into a single structure if multiple values must be returned

print foo(2,3) # (5, -1)
#print bar(2,3) # sorry, no dice