import tkinter as tk
from tkinter import (filedialog, messagebox, simpledialog)
import subprocess

root = tk.Tk()
root.title("Python Text Editor 1.0")
root.geometry("+250+340")
root.iconbitmap("python_18894.ico")

# FUNCTIONS
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if file_path:
        with open(file_path, "r") as file:
            code_text.delete(1.0, tk.END)
            code = file.read()
            code_text.insert(1.0, code)

def save_file():
    pass

# EDIT 
def cut_text():
    code_text.event_generate("<<Cut>>")
def copy_text():
    code_text.event_generate("<<Copy>>")
def paste_text():
    code_text.event_generate("<<Paste>>")
def clear_text():
    code_text.delete(1.0, tk.END)

def about():
    messagebox.showinfo("About", "This is a simple text editor built with Tkinter.")

def help():
    messagebox.showinfo("Help", "This is a simple text editor. Use the menu to open, save, cut, copy, and paste text.")

# RUN CODE 
def run_code():
    code = code_text.get(1.0, "end-1c")
    with open(".temp_code.py", "w") as file:
        file.write(code)
    result = subprocess.run(["python", ".temp_code.py"], capture_output=True)
    terminal_text.insert(tk.END, result.stdout.decode())
    terminal_text.insert(tk.END, result.stderr.decode())


def clear_code():
    terminal_text.delete(1.0, tk.END)

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


# RUN
run_menu = tk.Menu(menu, tearoff=False)
run_menu.add_command(label="Run", command=run_code)
run_menu.add_command(label="Clear Terminal", command=clear_code)
menu.add_cascade(label="Run", menu=run_menu)


# TEXT AREA CODE
text_frame = tk.Frame(root)
text_frame.pack(side = tk.LEFT, fill=tk.BOTH, expand=True)
code_text = tk.Text(text_frame)
code_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# CODE SCROLL BAR
text_scrollbar = tk.Scrollbar(text_frame, command = code_text.yview, orient = tk.VERTICAL)
text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
code_text.config(yscrollcommand = text_scrollbar.set)

# TEXT AREA TERMINAL
terminal_frame = tk.Frame(root)
terminal_frame.pack(side = tk.RIGHT, fill=tk.BOTH, expand=True)
terminal_text = tk.Text(terminal_frame, bg = "black", fg = "white", insertbackground = "white")
terminal_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# TERMINAL SCROLL BAR
terminal_scroll = tk.Scrollbar(terminal_frame, command = terminal_text.yview, orient = tk.VERTICAL)
terminal_scroll.pack(side=tk.RIGHT, fill=tk.Y)
terminal_text.config(yscrollcommand = terminal_scroll.set)


root.config(menu=menu)

root.mainloop()
