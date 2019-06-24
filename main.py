# -*- coding:utf -8 -*-
import os, glob
# from PIL import Image
import tkinter as tk
from tkinter import ttk

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Image Resizer")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()