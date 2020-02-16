from tkinter import Tk, Menu
from gui.merger_gui import show_merger_dialog
from gui.splitter_gui import show_splitter_dialog
from gui.deleter_gui import show_deleter_dialog

# Definitions
def present_layout(option):
  return 

def start():
  # Variables
  window = Tk()
  menu_bar = Menu(window)

  # Function select menu
  functions_menu = Menu(menu_bar, tearoff=0)
  functions_menu.add_command(label="Merge PDFs", command=lambda: show_merger_dialog(window))
  functions_menu.add_command(label="Split PDF", command=lambda: show_splitter_dialog(window))
  functions_menu.add_command(label="Delete pages from PDF", command=lambda: show_deleter_dialog(window))
  functions_menu.add_command(label="Extract part of a PDF", command=present_layout)

  # Add menus to the menubar
  menu_bar.add_cascade(label="Functions", menu=functions_menu)

  # Add menu bar to window
  window.config(menu=menu_bar)

  # Set window title
  window.title("PDF tools")

  # Set window size
  window.geometry("400x300")

  # Init window
  window.mainloop()