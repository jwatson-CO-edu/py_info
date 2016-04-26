## fileChoose3.py
## James Watson, March 2009
## A program to navigate the filesystem in Windows using Python and Tkinter

## -- CHANGE LOG --
## 03-25-09: Added capability to move back up file tree
## 03-26-09: Encapsulated file chooser as an object, this remedies the need for global variables
## 03-26-09: Added a second file chooser pane, made trivial by the above change
## -- TO DO --
## * Enhance capability to move about directories using os.path.walk()
## * Generalize this program across platforms
## * Add functions for Move, Copy, Delete
## * Allow for capability to select and act on multiple files
## * Add advanced sort and pattern features
## * Save scrollbar position moving up file tree (save scrollbar in all visited folders per session?)
## * Show filepath to each file pane

from Tkinter import *  # 
import os

# listbox1.insert(END, enter1.get())
# index = listbox1.curselection()[0]
# listbox1.delete(index)
# listbox1.delete(index)
# listbox1.insert(index, enter1.get())
# listbox1.delete(0, tk.END)

class FilePane(object):
    """ Object for moving through filesystem. Requires 2x2 on grid. Row = 0, Col = 0 grid offsets """
    def __init__(self, rootWindow, statusEntry, Row = 0, Col = 0):
        self.dirStr = ""
        self.dirToken = "/"
        self.root = rootWindow
        self.startRow = Row
        self.startCol = Col
        self.statusE = statusEntry
        # Create the UP button
        self.bttn_Up = Button(self.root, text = 'UP', command = self.up_level)
        self.bttn_Up.grid(row = self.startRow + 0, column = self.startCol + 0, sticky = W)
        # Create the address bar
        self.enty_AddrBar = Entry(root, width=40)
        self.enty_AddrBar.grid(row= self.startRow + 0, column= self.startCol + 0, sticky = E)
        self.enty_AddrBar.bind('<Return>', self.enter_path)
        self.enty_AddrBar.insert(0, 'Top Level.  Enter path.')
        # Create the listbox
        self.lsbx_Select = Listbox(self.root, width=50, height=6)
        self.lsbx_Select.grid(row = self.startRow + 1, column = self.startCol + 0)
        # Create the Listbox Scrollbar
        self.yscl_Move = Scrollbar(command = self.lsbx_Select.yview, orient = VERTICAL)
        self.yscl_Move.grid(row = self.startRow + 1, column = self.startCol + 1, sticky = N+S)
        # Associate scrollbar with listbox
        self.lsbx_Select.configure(yscrollcommand = self.yscl_Move.set)
        # Run function on doubleclick to open directory
        self.lsbx_Select.bind('<Double-Button-1>', self.clicky_dir)
    def window_drives(self):
        volumes = []
        # The following segment is for Windows, finds only drives named with uppercase char
        for i in range(ord('a'), ord('z')+1): # iterate over Unicode #s for a-z
            drive = chr(i).upper() + ":"
            if os.path.isdir(drive): # test if drive letter is a valid directory
                volumes.append(drive)
        return volumes
    def refresh_drives(self):
        # Load the listbox with drive names
        self.lsbx_Select.delete(0, END)
        for item in self.window_drives():
            self.lsbx_Select.insert(END, item)
    def reset_dir(self,newDir):
        if os.path.isdir(newDir):
            self.dirStr = newDir
            self.lsbx_Select.delete(0, END)
            self.enty_AddrBar.delete(0, END)
            self.enty_AddrBar.insert(0, newDir)
            for item in os.listdir(newDir):
                self.lsbx_Select.insert(END, item)
        else:
            self.statusE.delete(0, END)
            self.statusE.insert(0, "FilePane.reset_dir: Not a directory, " + newDir)
    def clicky_dir(self,event):
        index = self.lsbx_Select.curselection()[0]
        newDir = self.dirStr + self.lsbx_Select.get(index) + self.dirToken
        self.reset_dir(newDir)
    def up_level(self):
        newDir = self.dirStr[:-1]
        foundToken = False
        try:
            while not foundToken:
                if newDir[-1] != self.dirToken:
                    newDir = newDir[:-1]
                else:
                    foundToken = True
            self.reset_dir(newDir)
        except(IndexError):
            self.refresh_drives()
            self.dirStr = ""
    def enter_path(self,event):
        self.reset_dir(self.enty_AddrBar.get())
   
def transfer():
    pass


# Initialize Tkinter
root = Tk()
root.title("Directory Walker")

# Create the Left Transfer button
bttn_leTran = Button(root, text = '<--', command = transfer)
bttn_leTran.grid(row = 1, column = 2, sticky = NW)   

# Create the Right Transfer button
bttn_riTran = Button(root, text = '-->', command = transfer)
bttn_riTran.grid(row = 1, column = 2, sticky = SW)

# Create a status text box
enty_Status = Entry(root, width=50)
enty_Status.grid(row=3, column=0)
enty_Status.insert(0, 'Directory Walker by James Watson')

leftPane = FilePane(root, enty_Status)
rightPane = FilePane(root, enty_Status, Col = 3)

# Load the list of drives
leftPane.refresh_drives()
rightPane.refresh_drives()

# Start the graphic tkinter window
root.mainloop()

## enter1 = tk.Entry(root, width=50, bg='yellow')
## enter1.insert(0, 'Click on an item in the listbox')
## enter1.grid(row=1, column=0)
## # pressing the return key will update edited line
## enter1.bind('<Return>', set_list)
## # or double click left mouse button to update line
## enter1.bind('<Double-1>', set_list)
## enter1.get()
## enter1.delete(0, 50)
## enter1.insert(0, seltext)