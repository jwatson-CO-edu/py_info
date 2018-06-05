#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Template Version: 2017-04-13

# ~~ Future First ~~
from __future__ import division # Future imports must be called before everything else, including triple-quote docs!

"""
RESULT: A LOCAL FUNCTION CANNOT MODIFY THE LOCAL VARIABLES OF THE ENCLOSING FUNCTION, BUT WE CAN CHEAT BY ASSIGNING VALUES TO THE FUNCTION
        OBJECT ITSELF, AND MODIFY THOSE WITH THE ENCLOSED FUNCTION
"""

def swap_inside( A , B ):
    """ Demonstrate modifying function vars with a local function """
    swap_inside.a = A
    swap_inside.b = B
    
    def swap_a_b():
        """ Swap the function members """
        temp = swap_inside.a
        swap_inside.a = swap_inside.b
        swap_inside.b = temp
        
    print "Before swap:" , swap_inside.a , swap_inside.b
    swap_a_b()
    print "After swap: " , swap_inside.a , swap_inside.b
    
swap_inside( 1 , 2 )
# ~~ OUTPUT ~~
# Before swap: 1 2
# After swap:  2 1