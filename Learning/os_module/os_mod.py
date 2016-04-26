import os
from Tkinter import *

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        ## Note that in order for the creation of a widget to return a reference
        ## you must create the widget, and then invoke the 'grid' manager from
        ## the widget in separate statements.  If you use
        ## widgetVar = Widget(options).grid(options)
        ## then 'widgetVar' will have been assigned 'None'
        self.lbl_curDir = Label(self,
            text = os.getcwd()
            )
        self.lbl_curDir.grid(row = 0, column = 0, sticky = W)
        self.lbx_dirCon = Listbox(self,
            height = 15)
        self.lbx_dirCon.grid(row = 1, column = 0, sticky = W)
        self.yScroll = Scrollbar(self, orient = VERTICAL, 
            command = self.lbx_dirCon.yview)
        self.yScroll.grid(row = 1, column = 1, sticky = N+S+E)
        self.lbx_dirCon.configure(yscrollcommand = self.yScroll.set)
        for i in os.listdir(os.getcwd()):
            self.lbx_dirCon.insert(END, i)
    
    
root = Tk()
root.title('Python File Browser')
app = Application(root)
root.mainloop()