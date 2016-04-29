# -*- coding: utf-8 -*-

import Tkinter

topWin = Tkinter.Tk()

canvas = Tkinter.Canvas(topWin, bg='blue', height=250, width=300)
coord = (10,50,240,210)
arc = canvas.create_arc(coord,start=0,extent=150,fill='red')

canvas.pack()
topWin.mainloop()