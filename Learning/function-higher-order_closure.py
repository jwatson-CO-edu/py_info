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