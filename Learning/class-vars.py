# -*- coding: utf-8 -*-

"""
RESULTS
1. Can access a class member via an object via 'self.__class__.MEMBERNAME' , so that you don't have to use the class name over and over
"""

def sep(title = ""):
    print "=======" + ' ' + title + ' ' + "======="

class Xur(object):
    thing = 1
    
    def __init__( self ):
        pass
    
    def get_class_thing( self ):
        return self.__class__.thing

class TaggedObject(object):
    objName = "TaggedObject"
    totalInstance = 0
    def genTag(self):
        self.__class__.totalInstance += 1
        self.tag = self.objName + '_' + str(self.__class__.totalInstance)
    def __init__(self):
        self.genTag()

class Node(TaggedObject):
    # Note that __init__ is inherited from the parent class if it is not defined
    objName = "Node"   # 
    totalInstance = 0
    
gim = Xur()
print gim.get_class_thing() # 1
    
foo = TaggedObject()
print foo.tag
bar = Node()
print bar.tag
baz = TaggedObject()
qux = TaggedObject()
sep('Object Collection')
print foo.tag # same TaggedObject as above
print bar.tag # same Node as above
print baz.tag # new TaggedObject
print qux.tag # new TaggedObject