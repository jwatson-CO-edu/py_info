#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Return a list of strings that is each non-whitespace substring that is separated by at least one space ' ' """
split_by_spaces = lambda pStr: [ sub for sub in [item for item in pStr.split(' ') if item != ''] if not sub.isspace()]

print split_by_spaces('1   2    3      \t     \n      4') # ------------------------- ['1', '2', '3', '4']
print [float(item) for item in split_by_spaces('1   2    3      \t     \n      4')] # [1.0, 2.0, 3.0, 4.0]

def split_by_whitespace(pStr):
    """ Return a list of strings that were substrings separated by whitespace in the original string """
    tokenLst = []
    token = ''
    for char in pStr:
        if not char.isspace():
            token += char
        elif len(token) > 0:
            tokenLst.append(token)
            token = ''
    return tokenLst