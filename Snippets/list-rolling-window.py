#!/usr/bin/env python

class RollingList( list ): 
    """ A rolling window based on 'list' """ 
    
    def __init__( self , winLen , *args ):
        """ Normal 'list' init """
        list.__init__( self , [ 0 ] * winLen , *args )
        
    def append( self , item ):
        """ Append an item to the back of the list """
        list.append( self , item )
        del self[0]
        
    def prepend( self , item ):
        """ Prepend an item to the front of the list """
        self.insert( 0 , item )
        del self[-1]
        
    def get_average( self ):
        """ Get the rolling average , NOTE: Calling this function after inserting non-numeric data will result in an error """
        return sum( self ) * 1.0 / len( self )
        
    def item_list( self ):
        """ Return a copy of the RollingList as a list """
        return self[:]
    
if __name__ == "__main__":
    
    foo = RollingList( 3 )
    
    for i in xrange( 6 ):
        foo.append( i )
        print foo , foo.get_average()
        
    for i in xrange( 6 ):
        foo.prepend( i )
        print foo , foo.get_average()