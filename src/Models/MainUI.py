import tkinter as tk
from tkinter import Button, Label, ttk


class MainUI(tk.Tk):

    """Main window container"""

    def __init__(self , name) -> tk.Tk:
        super().__init__()
        self.style = ttk.Style(self)
        self.style.configure('TButton', font=('Helvetica', 12))
        self.style.configure('TLabel', font=('Helvetica', 12))
        self.geometry('280x230+50+50')
        self.title(name)
        self.setup_board()

    def some_func(self):
        # TODO: placeholder
        print(self.title)

    def setup_board(self):
        label1 = ttk.Label(text="Testing ")
        label1.grid(column=0, row=0)
        label1_entry1 = ttk.Entry()
        label1_entry1(column=0, row=1)
        reset_button = ttk.Button(text="\nRESET\n", command=self.some_func)
        reset_button.grid(column=1, row=0)
