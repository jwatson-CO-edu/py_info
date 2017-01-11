class Foo:
    """ A silly class for testing membership """
    
    def __init__( self ):
        """ Init some silly vars """
        self.bar = 1
        self.baz = 2
        
    def check_for_baz( self ):
        """ Check if this instance has a baz """
        return hasattr( self , 'baz' )
        
xur = Foo()

if hasattr( xur , 'bar' ):
    print "xur has a bar!" # xur has a bar!
    
if hasattr( xur , 'baz' ):
    print "xur has a baz!" # xur has a baz!
    
if hasattr( xur , 'ank' ):
    print "xur has an ank!"
else:
    print "xur has no ank!" # xur has no ank!
    
print "xur has a baz?:" , xur.check_for_baz()
    
"""
xur has a bar!
xur has a baz!
xur has no ank!
xur has a baz?: True
"""