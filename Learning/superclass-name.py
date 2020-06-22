import inspect



class Foo:
    def __init__( self ):
        self.a = 1
        
class Bar( Foo ):
    def __init__( self ):
        super().__init__()
        self.b = 2
        
baz = Bar()

def __name__in_tree( name , cls ):
    """ Return True if `name` appears anywhere in the class tree of `cls` """
    clsNames = [ elem.__name__ for elem in inspect.getmro( cls ) ]
    return name in clsNames

print( inspect.getmro( Bar ) )
print( inspect.getmro( baz.__class__ ) )
print( [ elem.__name__ for elem in inspect.getmro( baz.__class__ ) ] )
print( Foo )
print( Foo in inspect.getmro( Bar ) )
print( baz.__class__ in inspect.getmro( Bar ) )


print( "Is Foo a superclass of Bar?:" ,  __name__in_tree( Foo.__name__ , baz.__class__ ) )


########################################################################################################################

import enum

class Status(enum.Enum):
    """An enumerator representing the status of a behaviour """

    SUCCESS = "SUCCESS"
    """Behaviour check has passed, or execution of its action has finished with a successful result."""
    FAILURE = "FAILURE"
    """Behaviour check has failed, or execution of its action finished with a failed result."""
    RUNNING = "RUNNING"
    """Behaviour is in the middle of executing some action, result still pending."""
    INVALID = "INVALID"
    """Behaviour is uninitialised and inactive, i.e. this is the status before first entry, and after a higher priority switch has occurred."""
    
a = Status.SUCCESS

print( a.__class__ )
print( dir( a ) )
print( a.name , a.value )
print( type( a ) )