from tkinter import Toplevel, Button, Text
from tkinter import filedialog
from tkinter import END

# Let python get the files from project
import sys, os
sys.path.insert(0, os.path.abspath('..'))

from logic.deleter import deletePages, deleteRange
