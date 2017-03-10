def func_with_args( foo , bar , baz , **kwargs ):
    """ Simple function with three named args """
    print "Got named args:" , foo , bar , baz ,
    if 'other' in kwargs:
        print kwargs['other']
    else:
        print
    
argDict = { 'foo':1 , 'bar':2 , 'baz':3 , 'other':4 } # The dictionary will also populate '**kwargs'!

func_with_args( **argDict ) # Got named args: 1 2 3 4