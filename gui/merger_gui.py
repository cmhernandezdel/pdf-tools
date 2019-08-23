from tkinter import *
from tkinter import filedialog

filenames = []

def show_merge_button(root):


def add_file(root):
  filename = filedialog.askopenfilename()
  file_label = Text(root, height=1, width=30)
  file_label.pack()
  file_label.insert(END, filename)
  filenames.add(filename)
  if(len(filenames) == 2):
    show_merge_button(root)

def show_merger_dialog(root):
  merger_gui_window = Toplevel(root)
  add_button = Button(merger_gui_window, text="Add file", command=lambda: add_file(merger_gui_window))
  add_button.pack()