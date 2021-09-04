import tkinter as tk
import tkinter.filedialog as tkf
import os
import subprocess



root = tk.Tk()
root.withdraw() #use to hide tkinter window

currdir = os.getcwd()
tempfile = tkf.askopenfilename(parent=root, initialdir=currdir, title='Please select a file')
filename_f = os.path.basename(tempfile)
print(tempfile)
filename = filename_f.split(".")[0]
print(filename)
str_cmd = ' '.join(["g++", filename_f, "-o", filename])
print(str_cmd)
subprocess.run(str_cmd)
