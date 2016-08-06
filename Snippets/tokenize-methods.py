#!/usr/bin/env python
# -*- coding: utf-8 -*-

# == Separated with Space ==
print "hello      world \r   sample \t text".split() # ['hello', 'world', 'sample', 'text']

# == Separated with Character ==

print "hello,world,sample,text".split(',')           # ['hello', 'world', 'sample', 'text']
print "hello  ,  world,sample,text".split(',')       # ['hello  ', '  world', 'sample', 'text']     # Does not reject whitespace

# = Char Separated with Whitespace Rejection =

def tokenize_with_separator(rawStr,separator,evalFunc=str):
    """ Return a list of tokens taken from 'rawStr' that is partitioned with 'separator', transforming each token with 'evalFunc' """
    # TODO: Maybe this could be done with brevity using regex?
    tokens = [] # list of tokens to return
    currToken = '' # the current token, built a character at a time
    for char in rawStr: # for each character of the input string
        if not char.isspace(): # if the current char is not whitespace, process
            if not char == separator: # if the character is not a separator, then
                currToken += char # accumulate the char onto the current token
            else: # else the character is a separator, process the previous token
                tokens.append( evalFunc( currToken ) ) # transform token and append to the token list
                currToken = '' # reset the current token
        # else is whitespace, ignore
    if currToken: # If there is data in 'currToken', process it
        tokens.append( evalFunc( currToken ) ) # transform token and append to the token list
    return tokens
    
print tokenize_with_separator('1,2,3,4,5',',',float) # [1.0, 2.0, 3.0, 4.0, 5.0]

def tokenize_with_wspace( rawStr , evalFunc=str ):
    """ Return a list of tokens taken from 'rawStr' that is partitioned with whitespace, transforming each token with 'evalFunc' """
    # TODO: Maybe this could be done with brevity using regex?
    return [ evalFunc(rawToken) for rawToken in rawStr.split()]
    
print tokenize_with_wspace( "1   \r   2.5  \t  7.8" , float ) # [1.0, 2.5, 7.8]
