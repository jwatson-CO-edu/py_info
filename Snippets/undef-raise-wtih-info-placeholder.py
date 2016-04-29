# -*- coding: utf-8 -*-
import inspect, sys

def raiseNotDefined():
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print "*** Method not implemented: %s at line %s of %s" % (method, line, fileName)
    sys.exit(1)
    
def empty_func():
    raiseNotDefined()
    
empty_func() # *** Method not implemented: empty_func at line 13 of F:/Python/Snippets/undef-raise-wtih-info-placeholder.py