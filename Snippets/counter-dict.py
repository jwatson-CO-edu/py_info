class Counter(dict):
    """ The counter object acts as a dict, but sets previously unused keys to 0 , in the style of 6300 """
    # TODO: Add Berkeley / 6300 functionality
    
    def __init__( self , *args , **kw ):
        dict.__init__( self , *args , **kw )
        
    def __getitem__( self , a ):
        """ Get the val with key , otherwise return 0 if key DNE """
        if a in self: return dict.__getitem__( self , a )
        return 0
    
    # __setitem__ provided by 'dict'
    
        
foo = Counter()

print foo['dog'] # 0
foo['dog'] += 1
print foo['dog'] # 1
print foo[1] #     0
