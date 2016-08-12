f = lambda x: (x - 1.0) ** 2

def function_slope( f ):
    """ Return a function that estimates the slope of 'f'  """
    def slope( x , delta = 0.05 ):
        # run = 2 * delta
        # rise = f(x + delta) - f(x - delta)
        return ( f(x + delta) - f(x - delta) ) / ( 2 * delta )
    return slope
    
fdx = function_slope( f )

print f(2)   # 1.0
print fdx(2) # 2.0

def func_counter(incr):
    """ Return a function that counts """
    #counter = 0
    def func():
        count.counter += incr 
        # count += incr # Error: var referenced before assignment
        # For some reason cannot operate on the enclosed variable?
        print "'counter' state is", count.counter 
    count.counter = 0
    return func

foo = func_counter(1)
bar = func_counter(2)

foo() ; foo() ; foo() ; 
bar() ; bar() ; bar() ; 
"""
'counter' state is 1 <--- 'foo' counter
'counter' state is 2
'counter' state is 3
'counter' state is 2 <--- 'bar' counter
'counter' state is 4
'counter' state is 6
"""