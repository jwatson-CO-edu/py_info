# -*- coding: utf-8 -*-

"""
RESULTS: 
1. Functions defined with the '@classmethod' decorator have access to class variables via their first argument, which is always a reference 
   to the class.
2. Class methods are inherited. If the derived class has changed the inherited class variable to a different value, the inherited class
   method will correctly retrieve the value for the derived class, even though the method itself was defined in the parent class.
"""

class Foo(object):
    """ A dummy class """
    thing = 1
    secret = -1
    
    def __init__( self ):
        pass
    
    @classmethod #       v-- When method is defined with the '@classmethod' decorator, it is called with a class reference as the first arg
    def get_class_thing( clss ):
        return clss.thing # Return the class variable 'Foo.thing'.  Not having to use the actual class name is a benefit for when the class 
                          # is inherited, and the derived class has its own 'thing'. See below
                          
class Baz(Foo):
    thing = 2
    
    @classmethod
    def get_class_secret( clss ):
        return clss.secret # Secret comes from the parent class , it is inherited by the derived class
    
bar = Foo()
print bar.get_class_thing() # 1
xur = Baz()
print xur.get_class_thing() # 2
print xur.get_class_secret() # -1