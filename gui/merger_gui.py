from tkinter import *
from tkinter import filedialog

def add_file():
  filename = filedialog.askopenfilename()
  print('Added: ', filename)

def show_merger_dialog():
  window = Tk()
  add_button = Button(window, text="Add file", command=add_file)
  add_button.pack()
  window.mainloop()