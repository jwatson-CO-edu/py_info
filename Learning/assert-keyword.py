"""
RESULT: If the conditional following the 'assert' keyword evaluates False , then an 'AssertionError' is raised , Just like C++
        You can optionally provide a message string to give more information about the assertion was violated , which is a good idea anyway
"""

def picky_arg( arg ):
    """ 'arg' must be greater than 5 """
    assert arg > 5 , "'arg' was too small!"
    print "You make a compelling argument"
    
# picky_arg( 4 ) # AssertionError: 'arg' was too small! , program crashes with unhandled exception
picky_arg( 6 ) # "You make a compelling argument"