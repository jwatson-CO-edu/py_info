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
    
foo = RefTest()
bar = foo.get_dct()

bar['a'] = 5

print( foo.secret )