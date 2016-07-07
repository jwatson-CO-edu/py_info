class foo(object):
    def __init__(self, pSize):
        self.size = pSize
    def get_size(self):
        return self.size
    
thing1 = foo(20)
thing2 = foo(200)

print thing1.get_size # <bound method foo.get_size of <__main__.foo object at 0x7f3dafb657d0>>
print thing2.get_size # <bound method foo.get_size of <__main__.foo object at 0x7f3dafb65890>>
print foo.get_size    # <unbound method foo.get_size>

# URL, get a number identifying an object: https://docs.python.org/2/library/functions.html#id

print id(thing1) # 140714214729680
print id(thing2) # 140714214729872 # Each isntance is stored at a different location
print id(foo)    # 32113440        # The class is stored in its own location

print id(thing1.get_size) # 140689299144864
print id(thing2.get_size) # 140689299144864
print id(foo.get_size)    # 140689299144864 # Apparently the member functions are all stored at the same
#                                             location. Therefore, each instance does not recieve a copy
#                                             of the member function. That would take up a lot of space