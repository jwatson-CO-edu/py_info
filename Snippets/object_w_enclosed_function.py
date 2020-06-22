class Encloser:
    
    def __init__( self , capturedFunc ):
        """ Enclose a function in a member closure """
        def rtn_func():
            return capturedFunc
        self.closure = rtn_func
        
    def get_closure( self ):
        """ Return the function enclosed in the member var """
        return self.closure()
  
def say_msg():
    """ A silly function """
    print( "This is the message." )
  
foo = Encloser( say_msg )
bar = foo.get_closure()

bar()