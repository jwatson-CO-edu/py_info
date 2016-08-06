func = lambda x, y: (x, y)
print func.__code__.co_argcount #           2
print func.__code__.co_argcount.__class__ # <type 'int'>
print func.__code__.co_varnames #           ('x', 'y')
print func.__code__.__class__ #             <type 'code'>