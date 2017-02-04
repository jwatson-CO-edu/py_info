# URL, inspect the arguments passed to a function: http://stackoverflow.com/a/582097/893511

def func1(a,b,c):
    """ Inspect positional arguments """
    print locals().keys() # - ['a', 'c', 'b'] 
    print locals().values() # [1, 3, 2]
    print locals() # -------- {'a': 1, 'c': 3, 'b': 2}

def func2(*args):
    """ Inspect arbitrary arguments """
    print locals().keys() # - ['args'] 
    print locals().values() # [(1, 2, 3)]
    print locals() # -------- {'args': (1, 2, 3)}
    
def unpack_func( *args ):
    for item in args: print item ,
    print
    
print 'func1:' 
func1(1,2,3)

print

print 'func2:'
func2(1,2,3)

print 

unpack_func( *(1,2,3,4) ) # 1 2 3 4
unpack_func( *[5,6,7,8] ) # 5 6 7 8