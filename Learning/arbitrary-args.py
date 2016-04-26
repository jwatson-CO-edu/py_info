# -*- coding: utf-8 -*-

class multArgs(object):
    def __init__(self, arg1, *args2):
        self.firstArg = arg1
        self.restArgs = args2
        
foo = multArgs(1, 'a','b','c')
print foo.firstArg # 1
print foo.restArgs # ('a', 'b', 'c') # Stored as a tuple instead of a list

bar = multArgs(2, *['d','e','f'])
print bar.firstArg # 2
print bar.restArgs # ('d', 'e', 'f') # Stored as a tuple instead of a list

#foo.restArgs[1] = 3 # TypeError: 'tuple' object does not support item assignment

class multArgsAsList(object):
    def __init__(self, arg1, *args2):
        self.firstArg = arg1
        self.restArgs = list(args2) # conversion of tuple to list
        
baz = multArgsAsList(3, 'g','h','i')
baz.restArgs[1] = 3
print baz.firstArg # 3
print baz.restArgs # ['g', 3, 'i'] # 'args2' is stored as a mutable list