from tkinter import Toplevel, Button, Text, Entry, Label
from tkinter import filedialog
from tkinter import END

# Let python get the files from project
import sys, os
sys.path.insert(0, os.path.abspath('..'))

from logic.deleter import deletePages, deleteRange

filename = None

# Add a file
def add_file(root):
  global filename
  filename = filedialog.askopenfilename()
  file_label = Text(root, height=1, width=30)
  file_label.pack()
  file_label.insert(END, filename)

def show_deleter_dialog(root):
  deleter_gui_window = Toplevel(root)
  deleter_gui_window.geometry("400x300")

  add_button = Button(deleter_gui_window, text="Select file", command=lambda: add_file(deleter_gui_window))
  pages_text_field = Entry(deleter_gui_window)
  delete_button = Button(deleter_gui_window, text="Delete pages", command=lambda: deletePages(filename, pages_text_field.get()))
  label_text = "Select pages, e.g.: 1, 5, 6 or 3-7"
  label = Label(deleter_gui_window, text=label_text, height=4)
  
  
  add_button.pack()
  label.pack()
  pages_text_field.pack()
  delete_button.pack()