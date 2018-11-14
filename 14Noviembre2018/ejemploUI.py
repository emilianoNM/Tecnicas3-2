import tkinter as tk
from tkinter import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="bottom")
        self.hi_there.bind("<Key>", self.key)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="top")
       
        #v=StringVar()

        self.text=tk.Entry(self,width=10)
        self.text.bind("<Key>", self.key)
        self.text.pack(side='top')

    def say_hi(self):
        print("hi there, everyone!")
    def key(self,event):
        print ("pressed", event)


root = tk.Tk()
app = Application(master=root)
print('inicio de ventana')
app.mainloop()
print ('adios')