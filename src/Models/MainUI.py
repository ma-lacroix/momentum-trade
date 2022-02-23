import tkinter as tk
from tkinter import Button, Label, END, Entry, ttk


class MainUI(tk.Tk):

    """Main window container"""

    def __init__(self , name) -> tk.Tk:
        super().__init__()
        self.style = Style(self)
        self.style.configure('Button', font=('Arial', 12))
        self.style.configure('Label', font=('Arial', 12))
        self.geometry("400x300+10+10")
        self.lbl1 = Label(text='First number')
        self.lbl2 = Label(text='Second number')
        self.lbl3 = Label(text='Result')
        self.title(name)
        self.t1 = Entry(bd=3)
        self.t2 = Entry()
        self.t3 = Entry()
        self.btn1 = Button(text='Add')
        self.btn2 = Button(text='Subtract')
        self.lbl1.place(x=10, y=50)
        self.t1.place(x=100, y=50)
        self.lbl2.place(x=10, y=100)
        self.t2.place(x=100, y=100)
        self.b1 = Button(text='Add', command=self.add)
        self.b2 = Button(text='Subtract')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=10, y=150)
        self.b2.place(x=100, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))

    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))

