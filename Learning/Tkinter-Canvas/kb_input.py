# URL , keyboard and mouse input: http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
# URL , kb event symbols: https://docstore.mik.ua/orelly/other/python/0596001886_pythonian-chp-16-sect-9.html

from Tkinter import *

root = Tk()

def key( event ):
    print "event.char:" , repr( event.char ) , "event.keysym:" , event.keysym
    if event.keysym in ( "Up" , "Down" , "Left" , "Right" ):
		print "ARROWED!"

def callback( event ):
    frame.focus_set()
    print "clicked at" , event.x , event.y

# Tkinter window
frame = Frame( root , width = 300 , height = 300 )

# Bind callbacks to specific types of events
frame.bind( "<Key>"      , key      )
frame.bind( "<Button-1>" , callback )

# Prepare window
frame.pack()

# Start event loop
root.mainloop()
