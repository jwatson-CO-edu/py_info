#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

# Note all the controls below have the Frame as their parent. When they are packed into a grid, that grid applies to the
# interior of the frame

def init_controls(self):
    """ Control sliders """ 
    self.controlPanel = Frame(self.rootWin)
    # Control Sliders, Tkinter calls them 'Scale'
    j1_sldr = Scale(self.controlPanel, from_=-170, to=170, orient=HORIZONTAL) #Theta1 > 170 or Theta1 < -170:
    j2_sldr = Scale(self.controlPanel, from_=-190, to= 45, orient=HORIZONTAL) #Theta2 >  45 or Theta2 < -190:
    j3_sldr = Scale(self.controlPanel, from_=-120, to=156, orient=HORIZONTAL) #Theta3 > 156 or Theta3 < -120:
    j4_sldr = Scale(self.controlPanel, from_=-185, to=185, orient=HORIZONTAL) #Theta4 > 185 or Theta4 < -185:
    j5_sldr = Scale(self.controlPanel, from_=-120, to=120, orient=HORIZONTAL) #Theta5 > 120 or Theta5 < -120:
    j6_sldr = Scale(self.controlPanel, from_=-350, to=350, orient=HORIZONTAL) #Theta6 > 350 or Theta5 < -350:
    # Control Labels
    j1_labl = Label(self.controlPanel, text="Joint 1")
    j2_labl = Label(self.controlPanel, text="Joint 2")
    j3_labl = Label(self.controlPanel, text="Joint 3")
    j4_labl = Label(self.controlPanel, text="Joint 4")
    j5_labl = Label(self.controlPanel, text="Joint 5")
    j6_labl = Label(self.controlPanel, text="Joint 6")
    # Pack all widgets
    j1_sldr.grid(row=2, column=1); j2_sldr.grid(row=2, column=2); j3_sldr.grid(row=2, column=3); # Joint controls 1-3
    j1_labl.grid(row=3, column=1); j2_labl.grid(row=3, column=2); j3_labl.grid(row=3, column=3); # Slider labels  1-3
    j4_sldr.grid(row=4, column=1); j5_sldr.grid(row=4, column=2); j6_sldr.grid(row=4, column=3); # Joint controls 4-6 
    j4_labl.grid(row=5, column=1); j5_labl.grid(row=5, column=2); j6_labl.grid(row=5, column=3); # Slider labels  4-6
    self.controlPanel.grid(row=1,column=2) # Pack the control panel