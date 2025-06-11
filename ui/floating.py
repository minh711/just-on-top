import os
import platform
import tkinter as tk
from ui.drag import start_drag, do_drag

def create_floating_window(root):
    top = tk.Toplevel(root)
    top.attributes('-topmost', True)
    top.overrideredirect(True)
    top.configure(bg='#4A90E2')
    top.wm_attributes('-alpha', 0.8)

    label_text = tk.Label(
        top,
        text="Your text here",
        font=('Helvetica', 12, 'bold'),
        fg='white',
        bg='#4A90E2',
        padx=10,
        pady=10,
        justify='left',
        anchor='w',
        bd=0,
        relief='flat',
        wraplength=300
    )
    label_text.place(relx=0, rely=0, anchor='nw', x=10, y=10)

    # Force geometry calculation
    top.update_idletasks()

    # Get requested size of label
    label_width = label_text.winfo_reqwidth()
    label_height = label_text.winfo_reqheight()

    # Set window size to label size + padding (10px on each side)
    padding = 10
    window_width = label_width + padding * 2
    window_height = label_height + padding * 2
    top.geometry(f"{window_width}x{window_height}")

    # Get screen dimensions
    screen_width = top.winfo_screenwidth()

    # Calculate top-right corner position with 10px padding
    x = screen_width - window_width - 10
    y = 10

    # Apply final position
    top.geometry(f"{window_width}x{window_height}+{x}+{y}")

    top.bind("<ButtonPress-1>", lambda e: start_drag(e, top))
    top.bind("<B1-Motion>", lambda e: do_drag(e, top))

    return top, label_text
