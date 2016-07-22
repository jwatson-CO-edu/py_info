class testContainer:
    def __init__(self):
        self.baz = None

class ManyDots:
    def __init__(self):
        self.foo = testContainer() # Created a container class to support deeper organization
        # cannot begin with 'self.foo.baz = 2', because Python will try to figure out what 'foo' is instead of
        #creating a free-form object on a whim
        self.foo.baz = 2
        
baz = ManyDots()