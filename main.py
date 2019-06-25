import os, glob
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog

from editImage import EditImage

class Main(tk.Frame):
  def __init__(self, root):
    super().__init__(root)
    self.init_main()

  def init_main(self):
    toolbar = tk.Frame(bg='#d7d8e0', bd=2)
    toolbar.pack(side=tk.TOP, fill=tk.X)

    self.add_img = tk.PhotoImage(file='resourses/images/add.gif')
    btn_open_add_image_dialog = tk.Button(toolbar, text='Добавить фото', command=self.open_add_image_dialog, bg='#d7d8e0', bd=0, compound=tk.TOP, image=self.add_img)
    btn_open_add_image_dialog.pack(side=tk.LEFT)

    self.delete_image = tk.PhotoImage(file='resourses/images/delete.gif')
    btn_delete_dialog = tk.Button(toolbar, text='Удалить', bg='#d7d8e0', bd=0, image=self.delete_image, compound=tk.TOP, command=self.open_delete_dialog)
    btn_delete_dialog.pack(side=tk.LEFT)

    self.tree = ttk.Treeview(self, columns=('ID', 'image_path', 'original_size', 'resized_size'), height=15, show='headings')

    self.tree.column("ID", width=30, anchor=tk.CENTER)
    self.tree.column("image_path", width=315, anchor=tk.CENTER)
    self.tree.column("original_size", width=150, anchor=tk.CENTER)
    self.tree.column("resized_size", width=150, anchor=tk.CENTER)

    self.tree.heading("ID", text="№")
    self.tree.heading("image_path", text="Путь до фото")
    self.tree.heading("original_size", text="Ориг. разрешение")
    self.tree.heading("resized_size", text="Измен. разрешение")

    self.tree.pack()

  def open_add_image_dialog(self):
    Add()

  def open_delete_dialog(self):
    pass

class Add(tk.Toplevel):
  def __init__(self):
    super().__init__(root)
    self.init_add()
    self.view = app

  def init_add(self):
    self.selected_file = None
    self.title("Добавить изображение")
    self.geometry("400x100+400+300")
    self.resizable(False, False)

    label_select_file = ttk.Label(self, text="Выберите файл:")
    label_select_file.place(x=20, y=22.5)

    self.btn_select_file = ttk.Button(self, text="Открыть", command=self.open_file_dialog)
    self.btn_select_file.place(x=120, y=20)

    self.label_selected_file = ttk.Label(self, text="Файл не выбран")
    self.label_selected_file.place(x=200, y=22.5)

    self.btn_cancel = ttk.Button(self, text="Отмена", command=None)
    self.btn_cancel.place(x=220, y=65)

    self.btn_ok = ttk.Button(self, text="Добавить", command=self.add)
    self.btn_ok.place(x=300, y=65)

    self.grab_set()
    self.focus_set()

  def open_file_dialog(self):
    file = filedialog.askopenfile(initialdir = "/", title = "Выберите файл", filetypes = [ ("jpeg files", "*.jpg") ])
    
    if file:
      self.selected_file = file.name
      self.btn_select_file.configure(text="Выбрано")
      self.label_selected_file.configure(text=self.selected_file.split("/")[-1])
      self.btn_ok.configure(command=self.destroy)
    else: self.selected_file = None

  def add(self):
    file_path = self.selected_file
    if file_path:
      print(file_path)
      # images.append(file_path)
      # print(images)
      self.destroy()

if __name__ == "__main__":
  root = tk.Tk()
  app = Main(root)
  app.pack()

  EditImage()

  root.title("Image Resizer")
  root.geometry("650x450+300+200")
  root.resizable(False, False)
  root.iconbitmap("resourses/images/favicon.ico")
  root.mainloop()