import heapq

class PriorityQueue(list): # Requires heapq
    """ Implements a priority queue data structure. """ 
    # NOTE: PriorityQueue does not allow you to change the priority of an item. You may insert the same item multiple times with different priorities. 
        
    def __init__( self , *args ):
        """ Normal 'list' init """
        list.__init__( self , *args )   
        self.count = 0
        self.s = set([])    
        
    def push( self , item , priority , hashable=None ):
        """ Push an item on the queue and automatically order by priority , optionally provide 'hashable' version of item for set testing """
        entry = ( priority , self.count , item )
        heapq.heappush( self , entry )
        self.count += 1
        if hashable:
            self.s.add( hashable ) 
    
    def contains( self , hashable ): 
        ''' Test if 'node' is in the queue '''
        return hashable in self.s

    def pop( self ):
        """ Pop the lowest-priority item from the queue """
        priority , count , item = heapq.heappop( self )
        return item
        
    def pop_with_priority( self ):
        """ Pop the item and the priority associated with it """
        priority , count , item = heapq.heappop( self )
        return item , priority

    def isEmpty(self):
        """ Return True if the queue has no items, otherwise return False """
        return len( self ) == 0
        
    # __len__ is provided by 'list'
        
    def unspool(self):
        """ Pop all items as two sorted lists, one of increasing priorities and the other of the corresponding items """
        vals = []
        itms = []
        while not self.isEmpty():
            item , valu = self.pop_with_priority()
            vals.append( valu )
            itms.append( item )
        return itms , vals
    
foo = PriorityQueue()
foo.push( 'fish' ,  4 , 'fish' )
foo.push( 'dog' ,   1 , 'dog' )
foo.push( 'hog' ,   6 , 'hog' )
foo.push( 'cat' ,   2 , 'cat' )
foo.push( 'horse' , 5 , 'horse' )
foo.push( 'bird' ,  3 , 'bird' )


print foo.contains( 'dog' ) #    True
print foo.contains( 'cat' ) #    True
print foo.contains( 'dragon' ) # False

print foo.pop() # dog
print foo.pop_with_priority() # ('cat', 2)

items , vals = foo.unspool()

for i in range( len( items ) ):
    print items[i] , vals[i]
    
# print foo.pop() # ERROR: Cannot pop from an empty queue
    
"""
bird 3
fish 4
horse 5
hog 6
"""