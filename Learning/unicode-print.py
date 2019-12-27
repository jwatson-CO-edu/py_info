# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 10:39:22 2016

@author: JWatson
"""

print( u'\u0420\u043e\u0441\u0441\u0438\u044f' )
print( u" \u21D1 \u21d3 \u21d0 \u21d2 \u21d6 \u21d7 \u21d8 \u21d9 " )
# print u"         "

UNICODEARRW = { 'r': u'\u21d2'      , 'se': u'\u21d8'     , 'd': u'\u21d3'      , 'sw': u'\u21d9'     , 'l': u'\u21d0'      , 'nw': u'\u21d6'    , 'u': u'\u21D1'     , 'ne': u'\u21d7'     }

for key , val in UNICODEARRW.items():
    print( key , '\t' , val )