import tkinter as tk

#Creating the class
class Calculator:
    def __init__(self):
        self.window = tk.TK()
        self.window.geometry("375x667")
        self.window.resizeable(0,0)
        self.window.title("Calculator")