# def mixed_args( positional1 , positional2, **kwargs, *listArgs): # ERROR: **keywordArgs cannot appear before *listArgs
def mixed_args( positional1 , positional2 , *listArgs , **kwargs ):
    print "positional1:" , positional1
    print "positional2:" , positional2
    print listArgs
    print kwargs
    print locals()
    print
    
    
mixed_args('foo', 'bar') 
""" positional1: foo
    positional2: bar
    ()
    {}
    {'positional1': 'foo', 'listArgs': (), 'positional2': 'bar', 'kwargs': {}}                """

mixed_args('foo', 'bar', 'baz', 'qux')
""" positional1: foo
    positional2: bar
    ('baz', 'qux')
    {}
    {'positional1': 'foo', 'listArgs': ('baz', 'qux'), 'positional2': 'bar', 'kwargs': {}}    """

mixed_args('foo', 'bar', 'baz', 'qux', bears=40, bearType = 'polar')
""" positional1: foo
    positional2: bar
    ('baz', 'qux')
    {'bears': 40, 'bearType': 'polar'}
    {'positional1': 'foo', 'listArgs': ('baz', 'qux'), 'positional2': 'bar', 'kwargs': {'bears': 40, 'bearType': 'polar'}} """