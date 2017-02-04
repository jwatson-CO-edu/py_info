from random import randrange

def print_list( pList ):
    """ Print a list that is composed of the '__str__' of each of the elements in the format "[ elem_0 , ... , elem_n ]" , separated by commas & spaces """
    prnStr = "[ "
    for index , elem in enumerate( pList ):
        if index < len( pList ) - 1:
            prnStr += str( elem ) + " , "
        else:
            prnStr += str( elem ) + " ]"
    print prnStr
    
class Foo():
    def __init__( self ): # This is the color of a comment
        pass
    def __str__( self ):
        return str( randrange(40) )
        
theList = [ Foo() for i in xrange(10) ]

print theList #         [<__main__.Foo instance at 0x7f33175968c0>, <__main__.Foo instance at 0x7f33175962d8>, ...
print_list( theList ) # [ 17 , 29 , 2 , 8 , 20 , 31 , 21 , 27 , 34 , 17 ]