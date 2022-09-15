from tkinter import*
from tkinter import filedialog,messagebox,ttk
import os

class FileSelector:
			def __init__(self):
				pass
				
			def filePath(title=None):
				filepath=filedialog.	askopenfilename(filetypes=[("all files","*")],title=title,initialdir=os.curdir)
				return filepath
				
			def saveFile(title=None):
				savefile= filedialog.asksaveasfilename(filetypes=[("DAT","(*.dat)")],title=title,initialdir=os.pardir,defaultextension=".dat")
				return savefile
