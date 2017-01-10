#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Different way of accessing error information """

# Basic Error Info
try:
    foo = 1/0
except BaseException as err: # you can store a reference to an exception to access its text
	#  ^-- All exceptions inherit this one, useful if you want to print all errors
    print "You did a bad! , Msg: '" , err,"'"
    
# More detailed error info
try:
    foo = 1/0 
except Exception as ex: # URL, generic excpetions: http://stackoverflow.com/a/9824050
    print "Encountered" , type( ex ).__name__  ,  "with args:" , ex.args , "and with full text:" , str( ex )
