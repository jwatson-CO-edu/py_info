#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    foo = 1/0
except BaseException as err: # you can store a reference to an exception to access its text
	#  ^-- All exceptions inherit this one, useful if you want to print all errors
    print "You did a bad! , Msg: '" , err,"'"
