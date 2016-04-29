## fileChoose2.py
## James Watson, March 2009
## A program to navigate the filesystem in Windows using Python and Tkinter

## -- CHANGE LOG --
## 03-25-09: Added capability to move back up file tree
## -- TO DO --
## * Enhance capability to move about directories using os.path.walk()
## * Generalize this program across platforms
## * Find a way to access the directory without using globals (OOP?, each function belongs
## to an object that has its path stored in a variable?)
## * Add a second file tree pane

from Tkinter import *  # 
import os

# listbox1.insert(END, enter1.get())
# index = listbox1.curselection()[0]
# listbox1.delete(index)
# listbox1.delete(index)
# listbox1.insert(index, enter1.get())
# listbox1.delete(0, tk.END)

global leftDir
leftDir = ""
global dirToken
dirToken = "/"

def window_drives():
    volumes = []
    # The following segment is for Windows, finds only drives named with uppercase char
    for i in range(ord('a'), ord('z')+1): # iterate over Unicode #s for a-z
        drive = chr(i).upper() + ":"
        if os.path.isdir(drive): # test if drive letter is a valid directory
            volumes.append(drive)
    return volumes
    
def refresh_drives():
    # Load the Left listbox with drive names
    lsbx_Left.delete(0, END)
    for item in window_drives():
        lsbx_Left.insert(END, item)
    
def reset_Ldir(newDir):
    global leftDir
    if os.path.isdir(newDir):
        leftDir = newDir
        lsbx_Left.delete(0, END)
        for item in os.listdir(newDir):
            lsbx_Left.insert(END, item)
    
def clicky_dir(event):
    global leftDir
    global dirToken
    index = lsbx_Left.curselection()[0]
    newDir = leftDir + lsbx_Left.get(index) + dirToken
    reset_Ldir(newDir)
    
            
def up_level():
    global leftDir
    global dirToken
    newDir = leftDir[:-1]
    foundToken = False
    try:
        while not foundToken:
            if newDir[-1] != dirToken:
                newDir = newDir[:-1]
            else:
                foundToken = True
        reset_Ldir(newDir)
    except(IndexError):
        refresh_drives()
        leftDir = ""
    

# Initialize Tkinter
root = Tk()
root.title("Directory Walker")

# Create the UP button
bttn_up = Button(root, text = 'UP', command = up_level)
bttn_up.grid(row=0, column=0, sticky=W)

# Create the Left listbox
lsbx_Left = Listbox(root, width=50, height=6)
lsbx_Left.grid(row=1, column=0)
 
# Create the Left Listbox Scrollbar
yscl_Left = Scrollbar(command = lsbx_Left.yview, orient = VERTICAL)
yscl_Left.grid(row = 1, column = 1, sticky = N+S)
lsbx_Left.configure(yscrollcommand = yscl_Left.set)

# Run function on doubleclick to open directory
lsbx_Left.bind('<Double-Button-1>', clicky_dir)

# Load the list of drives
refresh_drives()
 
# Start the graphic tkinter window
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