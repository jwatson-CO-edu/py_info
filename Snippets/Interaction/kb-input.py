#!/usr/bin/env python
# -*- coding: utf-8 -*-

# URL , Read kb state in Python: https://rosettacode.org/wiki/Keyboard_input/Keypress_check#Python

import pygame
from pygame import key
from time import sleep

pygame.init()
sleep(2)
for i in range(10):
    print "Input from kb?:" , key.get_focused()
    #print key.get_pressed()
    #pygame.event.pump()
    #print pygame.event.get()
    print "How many pressed:" , sum( key.get_pressed() )
    print "'d' is pressed:" , key.get_pressed()[pygame.K_d]