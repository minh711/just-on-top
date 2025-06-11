import os
import platform
import tkinter as tk
from ui.drag import start_drag, do_drag

def create_floating_window(root):
    top = tk.Toplevel(root)
    top.attributes('-topmost', True)
    top.overrideredirect(True)
    top.configure(bg='#4A90E2')

    # Windows-specific transparency
    if platform.system() == "Windows":
        top.wm_attributes('-transparentcolor', top['bg'])

    label_text = tk.Label(
        top,
        top.wm_attributes('-alpha', 0.8),
        text="Your text here",
        font=('Helvetica', 12, 'bold'),
        fg='white',
        bg='#4A90E2', # Match window's background
        padx=10,
        pady=10,
        justify='left',
        anchor='w',
        bd=0,
        relief='flat',
        wraplength=300
    )
    label_text.place(relx=0, rely=0, anchor='nw', x=10, y=10)

    top.bind("<ButtonPress-1>", lambda e: start_drag(e, top))
    top.bind("<B1-Motion>", lambda e: do_drag(e, top))

    return top, label_text
