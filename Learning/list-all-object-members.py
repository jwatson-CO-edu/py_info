# -*- coding: utf-8 -*-

class Test(object):
    def __init__(self):
        self.foo = 1
        self.bar = 2
        
foo = Test()
foo.baz = 3

print vars(foo) # {'baz': 3, 'foo': 1, 'bar': 2}