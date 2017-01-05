# -*- coding: utf-8 -*-
import os , sys
SOURCEDIR = os.path.dirname( os.path.abspath( __file__ ) ) # URL, dir containing source file: http://stackoverflow.com/a/7783326
SOURCENAM = os.path.split( __file__ )[1]

print "Source for module:" , SOURCEDIR
print "Name for module:  " , SOURCENAM