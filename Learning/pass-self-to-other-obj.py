# -*- coding: utf-8 -*-

class Test(object):
    def __init__(self):
        self.foo = 1
        self.bar = 2
        self.parent = None
        self.msg = ""
    def give_ref(self, obj):
        obj.parent = self
    def parent_msg(self):
        print self.parent.msg
        
        
baz = Test()
qux = Test()
baz.msg = "child msg"
qux.msg = "parent msg"
qux.give_ref(baz)
baz.parent_msg() # "parent msg"