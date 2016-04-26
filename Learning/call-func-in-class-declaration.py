# -*- coding: utf-8 -*-

def cls_declare_print(clsName):
    print "Class",clsName,"was declared!"

class Foo(object):
    cls_declare_print('Foo')
    def __init__(self):
        print "One new Foo!"
        
class Bar(object):
    cls_declare_print('Bar')
    def __init__(self):
        print "One new Bar!"
        
theFoo = Foo()
theBar = Bar()
anotherFoo = Foo()
anotherBar = Bar()

# Class Foo was declared! # As expected, 'cls_declare_print' was only called once in the declaration of each class!
# Class Bar was declared!
# One new Foo!
# One new Bar!
# One new Foo!
# One new Bar!