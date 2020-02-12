from tkinter import Toplevel, Button, Text
from tkinter import filedialog
from tkinter import END

# Let python get the files from project
import sys, os
sys.path.insert(0, os.path.abspath('..'))

from logic.merger import merge_files

filenames = []

def add_file(root):
  filename = filedialog.askopenfilename()
  file_label = Text(root, height=1, width=30)
  file_label.pack()
  file_label.insert(END, filename)
  filenames.append(filename)

def show_merger_dialog(root):
  merger_gui_window = Toplevel(root)
  merger_gui_window.geometry("400x300")
  add_button = Button(merger_gui_window, text="Add file", command=lambda: add_file(merger_gui_window))
  merge_button = Button(merger_gui_window, text="Merge files", command=lambda: merge_files(filenames))
  add_button.pack()
  merge_button.pack()