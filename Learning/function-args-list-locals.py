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
    

print 'func1:' 
func1(1,2,3)

print

print 'func2:'
func2(1,2,3)