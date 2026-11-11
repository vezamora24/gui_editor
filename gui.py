import tkinter as tk
from tkinter import (filedialog, messagebox, simpledialog)
import subprocess

root = tk.Tk()
root.geometry("400x500+110+340")
root.iconbitmap("python_18894.ico")

# FUNCTIONS
def open_file():
    pass
def save_file():
    pass

# EDIT 
def cut_text():
    pass
def copy_text():
    pass    
def paste_text():
    pass
def clear_text():
    pass

def about():
    messagebox.showinfo("About", "This is a simple text editor built with Tkinter.")

def help():
    messagebox.showinfo("Help", "This is a simple text editor. Use the menu to open, save, cut, copy, and paste text.")


# NAVIGATION
navbar = tk.Frame(root)
navbar.pack(fill=tk.X)

# DROPDOWN MENU
menu = tk.Menu(navbar)

# BUTTONS

# FILES
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

# EDIT MENU
edit_menu = tk.Menu(menu, tearoff=False)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_command(label="Clear", command=clear_text)
menu.add_cascade(label="Edit", menu=edit_menu)

# ABOUT MENU
about_menu = tk.Menu(menu, tearoff=False)
about_menu.add_command(label="About", command=about)
menu.add_cascade(label="About", menu=about_menu)

# HELP MENU
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label="Help", command=help)
menu.add_cascade(label="Help", menu=help_menu)


root.config(menu=menu)

root.mainloop()
