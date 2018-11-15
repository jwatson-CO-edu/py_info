#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Template Version: 2017-04-13

# ~~ Future First ~~
from __future__ import division # Future imports must be called before everything else, including triple-quote docs!

"""
RESULT:
A python script and the python shell are separate processes, and you cannot share data between them.
To keep data in memory, the process must keep running. Memory belongs to the process running the script, NOT to the shell. 
The shell cannot hold memory for you.
"""

import sys , datetime

# === Main Application =====================================================================================================================

# = Program Functions =

def check_and_create_obj():
    """ Persistent functor """
    if not check_and_create_obj.stamp:
        check_and_create_obj.stamp = str( datetime.datetime.now() )
        print "NOT INITIALIZED , Logged time:" , check_and_create_obj.stamp
    else:
        print "FOUND INITIALIZED! , Good job!"
try:
    check_and_create_obj.stamp
    print "Test" , check_and_create_obj.stamp
except:
    check_and_create_obj.stamp = None
    
def check_and_set_var():
    """ Persistent functor that encloses a var? """
    global flag
    try:
        flag
        print "FOUND STORED! , Good job!"
    except:
        globals()['flag'] = str( datetime.datetime.now() )
        print "NOT STORED , Logged time:" , flag        
        
        

# _ End Func _

# = Program Vars =



# _ End Vars _

if __name__ == "__main__":
    termArgs = sys.argv[1:] # Terminal arguments , if they exist
    
    check_and_create_obj() # FUNCTOR MEMBER DID NOT PERSIST
    check_and_set_var()    # GLOBAL VAR ___ DID NOT PERSIST
    

# ___ End Main _____________________________________________________________________________________________________________________________
