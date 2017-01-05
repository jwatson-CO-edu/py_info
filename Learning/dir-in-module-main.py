# -*- coding: utf-8 -*-
import os , sys
SOURCEDIR = os.path.dirname( os.path.abspath( __file__ ) ) # URL, dir containing source file: http://stackoverflow.com/a/7783326
SOURCENAM = os.path.split( __file__ )[1]

print "Source for main:  " , SOURCEDIR , "before import" 
print "Name for main:    " , SOURCENAM , "before import" # dir-in-module-main.py before import
#                                                                        ----
from dir_in_module_module import *

print "Source for main:  " , SOURCEDIR , "after import" 
print "Name for main:    " , SOURCENAM , "after import" # dir_in_module_module.pyc after import
#                                                                       ------

SOURCEDIR = os.path.dirname( os.path.abspath( __file__ ) ) # URL, dir containing source file: http://stackoverflow.com/a/7783326
SOURCENAM = os.path.split( __file__ )[1]

print "Source for main:  " , SOURCEDIR , "after reset" 
print "Name for main:    " , SOURCENAM , "after reset" # dir-in-module-main.py after reset
#                                                                      ----