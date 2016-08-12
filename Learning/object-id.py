class thing:
    def __init__(self):
        self.num =4
    def rtn_id(self):
        return id(self)
    
foo = thing()
bar = thing()
baz = foo

print foo.rtn_id() # 140589619235368    # NOTE: These numbers will be different each run, 
print id(foo) #      140589619235368    #       What's important is that the id's are the same for same object during each run
print id(baz) #      140589619235368    # A variable that holds a reference to the same object has the same id

print bar.rtn_id() # 140589619235440
print id(bar) #      140589619235440