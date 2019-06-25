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
    toolbar = tk.Frame(bg='#d7d8e0', bd=2)
    toolbar.pack(side=tk.TOP, fill=tk.X)

    self.add_img = tk.PhotoImage(file='resourses/images/add.gif')
    btn_open_dialog = tk.Button(toolbar, text='Добавить фото', command=self.open_dialog, bg='#d7d8e0', bd=0, compound=tk.TOP, image=self.add_img)
    btn_open_dialog.pack(side=tk.LEFT)

    self.delete_image = tk.PhotoImage(file='resourses/images/delete.gif')
    btn_delete_dialog = tk.Button(toolbar, text='Удалить', bg='#d7d8e0', bd=0, image=self.delete_image, compound=tk.TOP, command=self.open_delete_dialog)
    btn_delete_dialog.pack(side=tk.LEFT)

  def open_dialog(self):
    Child()

  def open_delete_dialog(self):
    pass

class Child(tk.Toplevel):
  def __init__(self):
    super().__init__(root)
    self.init_child()
    self.view = app

  def init_child(self):
    self.title('Добавить доходы/расходы')
    self.geometry('400x220+400+300')
    self.resizable(False, False)

if __name__ == "__main__":
  root = tk.Tk()
  app = Main(root)
  app.pack()
  root.title("Image Resizer")
  root.geometry("650x450+300+200")
  root.resizable(False, False)
  root.iconbitmap("resourses/images/favicon.ico")
  root.mainloop()