import os, glob
# from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import Open

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
    self.title("Добавить изображение")
    self.geometry("400x220+400+300")
    self.resizable(False, False)

    label_select_file = ttk.Label(self, text="Выберите файл:")
    label_select_file.place(x=20, y=52.5)

    self.btn_select_file = ttk.Button(self, text="Открыть", command=self.add_to_list())
    self.btn_select_file.place(x=120, y=50)
    # self.btn_select_file.bind("<Button-1>", lambda event: self.add_to_list() )

    btn_cancel = ttk.Button(self, text="Отмена", command=self.destroy)
    btn_cancel.place(x=220, y=180)

    self.btn_ok = ttk.Button(self, text="Добавить")
    self.btn_ok.place(x=300, y=180)
    # self.btn_ok.bind('<Button-2>', lambda event: self.view.records(self.entry_description.get(), self.combobox.get(), self.entry_money.get()))

    self.grab_set()
    self.focus_set()

  def open_file_dialog(self):
    file = tk.filedialog.askopenfile(initialdir = "/", title = "Выберите файл", filetypes = [ ("jpeg files", "*.jpg") ])
    if (file): return file.name
    else: return None

  def add_to_list(self):
    file_path = self.open_file_dialog()
    if file_path: print(file_path)

if __name__ == "__main__":
  root = tk.Tk()
  app = Main(root)
  app.pack()
  root.title("Image Resizer")
  root.geometry("650x450+300+200")
  root.resizable(False, False)
  root.iconbitmap("resourses/images/favicon.ico")
  root.mainloop()