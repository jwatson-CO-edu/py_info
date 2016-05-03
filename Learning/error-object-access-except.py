#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    foo = 1/0
except ZeroDivisionError as err: # you can use this feature to access the text of the error
    print "You did a bad! , Msg: '" , err,"'"