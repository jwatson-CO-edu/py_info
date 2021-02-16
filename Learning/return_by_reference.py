class RefTest:
    """ Test class to see if the a reference to the dict or the dict itself is returned """
    
    def __init__( self ):
        """ Construct a "secret" dictionary """
        self.secret = {
            'a': 1,
            'b': 2
        }
        
    def get_dct( self ):
        """ Return the dict """
        return self.secret
    
foo = RefTest() # --- Construct an object that contains a dictionary
bar = foo.get_dct() # Fetch the dict
bar['a'] = 5 # ------ Attempt to modify dict

print( foo.secret ) # {'a': 5, 'b': 2}
# RESULT: Dict was modified, the member function returned a reference to the member object