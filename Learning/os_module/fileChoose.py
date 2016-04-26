# load a Tkinter listbox with data lines from a file,
# sort data lines, select a data line, display the data line,
# edit the data line, update listbox with the edited data line
# add/delete a data line, save the updated listbox to a data file
# used a more modern import to give Tkinter items a namespace
# tested with Python24       vegaseat       16nov2006

#!/usr/bin/env python

from Tkinter import *  # 
import os

# listbox1.insert(END, enter1.get())
# index = listbox1.curselection()[0]
# listbox1.delete(index)
# listbox1.delete(index)
# listbox1.insert(index, enter1.get())
# listbox1.delete(0, tk.END)

def window_drives():
    volumes = []
    # The following segment is for Windows, finds only drives named with uppercase char
    for i in range(ord('a'), ord('z')+1): # iterate over Unicode #s for a-z
        drive = chr(i).upper() + ":/"
        if os.path.isdir(drive): # test if drive letter is a valid directory
            volumes.append(drive)
    return volumes
    
def clicky_drive(event):
    index = lsbx_Left.curselection()[0]
    seltext = lsbx_Left.get(index)
    print "You doubleclicked drive " + seltext
 
# INITIALIZE Tkinter
root = Tk()
root.title("Directory Walker")

# CREATE THE LEFT LISTBOX
lsbx_Left = Listbox(root, width=50, height=6)
lsbx_Left.grid(row=0, column=0)
 
# CREATE THE SCROLLBAR FOR LEFT LISTBOX
yscl_Left = Scrollbar(command = lsbx_Left.yview, orient = VERTICAL)
yscl_Left.grid(row = 0, column = 1, sticky = N+S)
lsbx_Left.configure(yscrollcommand = yscl_Left.set)

# LOAD LIST WITH DRIVE NAMES
for item in window_drives():
    lsbx_Left.insert(END, item)
 
# RUN FUNCTION ON DOUBLECLICK OF OPTION
lsbx_Left.bind('<Double-Button-1>', clicky_drive)
 
# START THE GRAPHIC Tkinter WINDOW
root.mainloop()

## Another Example

## from Tkinter import *

## class Test(Tk):
    ## def __init__(self):
        ## Tk.__init__(self)
        ## l = Listbox(self)
        ## l.pack()
        ## l.insert('end', 'line 1')
        ## l.insert('end', 'line 2')
        ## l.insert('end', 'line 3')
        ## l.bind('<1>', self.dummy)
        ## l.bind('<Double-Button-1>', self.test)
## def dummy(self, event):
    ## return 'break'
## def test(self, event):
    ## print 'hello'

# Execute if this file is being run as a script
# If it is not being executed as 'main', it will act as a module
## if __name__ == '__main__':
    ## t = Test()
    
## t.mainloop()