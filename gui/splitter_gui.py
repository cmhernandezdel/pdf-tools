from tkinter import Toplevel, Button, Entry, Label
from tkinter import filedialog
from tkinter import END, LEFT, RIGHT

# Let python get the files from project
import sys, os
sys.path.insert(0, os.path.abspath('..'))

from logic.splitter import split_file

split_points = []

def add_file(root):
  filename = filedialog.askopenfilename()
  file_label = Text(root, height=1, width=30)
  file_label.pack()
  file_label.insert(END, filename)
  filenames.append(filename)

def show_splitter_dialog(root):
  splitter_gui_window = Toplevel(root)
  split_point_entry = Entry(splitter_gui_window)
  split_point_label = Label(splitter_gui_window, text="Add split point")
  add_point_button = Button(splitter_gui_window, text="Add", command=lambda: add_split_point(merger_gui_window))
  split_button = Button(splitter_gui_window, text="Split file", command=lambda: split_file(split_points))
  split_point_label.pack()
  split_point_entry.pack(side=LEFT)
  add_point_button.pack(side=RIGHT)