# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

    # www.python-course.eu/tkinter_canvas.php

from Tkinter import *

canvas_width = 400
canvas_height =400
python_green = "#476042"

def polygon_star(canvas, x,y,p,t, outline=python_green, fill='yellow', width = 1):
   points = []
   for i in (1,-1):
      points.extend((x,	       y + i*p))
      points.extend((x + i*t, y + i*t))
      points.extend((x + i*p, y))
      points.extend((x + i*t, y - i * t))

   print(points)

   canvas.create_polygon(points, outline=outline, 
                         fill=fill, width=width)

master = Tk()

w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

p = 50
t = 15

nsteps = 10
step_x = int(canvas_width / nsteps)
step_y = int(canvas_height / nsteps)

for i in range(1, nsteps):
   polygon_star(w,i*step_x,i*step_y,p,t,outline='red',fill='gold', width=3)
   polygon_star(w,i*step_x,canvas_height - i*step_y,p,t,outline='red',fill='gold', width=3)

mainloop()

#import Tkinter
#
#topWin = Tkinter.Tk()
#
#canvas = Tkinter.Canvas(topWin, bg='blue', height=250, width=300)
#coord = (10,50,240,210)
#arc = canvas.create_arc(coord,start=0,extent=150,fill='red')
#
#canvas.pack()
#topWin.mainloop()

#class Test(object):
#    def __init__(self):
#        self.foo = 1
#        self.bar = 2
#        self.parent = None
#        self.msg = ""
#    def give_ref(self, obj):
#        obj.parent = self
#    def parent_msg(self):
#        print self.parent.msg
#        
#        
#baz = Test()
#qux = Test()
#baz.msg = "child msg"
#qux.msg = "parent msg"
#qux.give_ref(baz)
#baz.parent_msg()

#print vars(foo) # {'baz': 3, 'foo': 1, 'bar': 2}

# FIXME : TEST USING REFERENCE TO CONTAINER


#class Num_Wrapper(object):
#    def __init__(self, num):
#        self.thing = num
#    def __str__(self):
#        return str(self.thing)
#        
#def str_list(lst):
#    rtnStr = ""
#    for elem in lst:
#        rtnStr += str(elem) + " "
#    return rtnStr
#        
#foo = [ Num_Wrapper(1), Num_Wrapper(2), Num_Wrapper(3) ]
#
#bar = [None] * len(foo)
#
#for i in range(len(foo)):
#    bar[i] = foo[i]
#    
#print str_list(foo)
#print str_list(bar)
#print "Change foo"
#foo[1] = Num_Wrapper(8)
#print str_list(foo)
#print str_list(bar)

#import math
#from Vector import Vector, Quat
#
#foo = Quat.k_rot_to_Quat([0,0,1], math.pi/4) 
#print str(foo.apply_to( Vector([1,0,1])))