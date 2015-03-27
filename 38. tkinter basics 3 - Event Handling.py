'''
Hello and welcome to a basic intro to TKinter, which is the Python
binding to TK, which is a toolkit that works around the Tcl language.

The tkinter module purpose to to generate GUIs, like windows. Python is not very
popularly used for this purpose, but it is more than capable of being used

'''


# Simple enough, just import everything from tkinter.
from tkinter import *


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Exit",command=self.client_exit)

        # placing the button on my window
        quitButton.place(x=0, y=0)

        


    def client_exit(self):
        exit()


        
        



# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()  

