from tkinter import *
import merger_gui

# Definitions
def present_layout(option):
  return 

# Variables
window = Tk()
menu_bar = Menu(window)

# Function select menu
functions_menu = Menu(menu_bar, tearoff=0)
functions_menu.add_command(label="Merge PDFs", command=lambda: merger_gui.show_merger_dialog(window))
functions_menu.add_command(label="Split PDF", command=present_layout)
functions_menu.add_command(label="Delete pages", command=present_layout)
functions_menu.add_command(label="Extract part of a PDF", command=present_layout)

# Add menus to the menubar
menu_bar.add_cascade(label="Functions", menu=functions_menu)

# Add menu bar to window
window.config(menu=menu_bar)

# Set window title
window.title("PDF tools")

# Init window
window.mainloop()