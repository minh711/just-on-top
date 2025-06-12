import os
import platform
import tkinter as tk  # must use tkinter so it will on top of all virtual desktops
from windows.floating_window.drag import start_drag, do_drag
from utils.constants import PADDING


def create_floating_window(root):
    top = tk.Toplevel(root)
    top.attributes("-topmost", True)
    top.overrideredirect(True)
    top.configure(bg="#4A90E2")
    # top.wm_attributes('-alpha', 0.8) # not works well with Linux

    default_text = "Your text here"

    label_text = tk.Label(
        top,
        text=default_text,
        font=("Helvetica", 12, "bold"),
        fg="white",
        bg="#4A90E2",
        justify="left",
        anchor="w",
        bd=0,  # bd=2
        relief="flat",  # relief='solid'
        wraplength=300,
    )
    label_text.place(relx=0, rely=0, anchor="nw", x=PADDING, y=PADDING)

    # Force geometry calculation
    top.update_idletasks()

    # Get requested size of label
    label_width = label_text.winfo_reqwidth()
    label_height = label_text.winfo_reqheight()

    # Set window size to label size + padding (10px on each side)
    window_width = label_width + PADDING * 2
    window_height = label_height + PADDING * 2
    top.geometry(f"{window_width}x{window_height}")

    # Get screen dimensions
    screen_width = top.winfo_screenwidth()

    # Calculate top-right corner position with 10px padding
    x = screen_width - window_width - PADDING
    y = PADDING

    # Apply final position
    top.geometry(f"{window_width}x{window_height}+{x}+{y}")

    top.bind("<ButtonPress-1>", lambda e: start_drag(e, top))
    top.bind("<B1-Motion>", lambda e: do_drag(e, top))

    return top, label_text
