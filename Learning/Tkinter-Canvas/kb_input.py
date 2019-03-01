from Tkinter import *

root = Tk()

def key(event):
    print "event.char:" , repr( event.char ) , "event.keysym:" , event.keysym
    if event.keysym in ( "Up" , "Down" , "Left" , "Right" ):
		print "ARROWED!"

def callback(event):
    frame.focus_set()
    print "clicked at", event.x, event.y

# Tkinter window
frame = Frame( root , width = 100 , height = 100 )

# Bind callbacks to specific types of events
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)

# Prepare window
frame.pack()

# Start event loop
root.mainloop()
