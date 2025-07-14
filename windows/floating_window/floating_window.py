import os
import platform
import tkinter as tk  # must use tkinter so it will on top of all virtual desktops
from windows.floating_window.drag import start_drag, do_drag
from utils.constants import (
    PADDING,
    BORDER_WIDTH,
    DEFAULT_COLOR,
    DEFAULT_BACKGROUND_COLOR,
    DEFAULT_CONTENT,
    DEFAULT_FONT_SIZE,
    DEFAULT_FONT,
)
from utils.settings import load_settings
from models.settings import Settings


def create_floating_window(root):
    settings: Settings = load_settings()
    bordered: int = settings.get("bordered", 1)
    color: str = settings.get("color", DEFAULT_COLOR)
    background_color: str = settings.get("background_color", DEFAULT_BACKGROUND_COLOR)
    content: str = settings.get("content", DEFAULT_CONTENT)
    if content == "":
        content = DEFAULT_CONTENT
    font_size: int = settings.get("font_size", DEFAULT_FONT_SIZE)
    font: str = settings.get("font", DEFAULT_FONT)

    top = tk.Toplevel(root)
    top.attributes("-topmost", True)
    top.overrideredirect(True)
    top.configure(bg=background_color)

    # top.wm_attributes('-alpha', 0.8) # not works well with Linux

    # Border color
    border_color = "#000000"

    # Create a frame to simulate border
    frame = tk.Frame(
        top,
        bg=border_color if bordered else background_color,
        bd=0,
        highlightthickness=0,
    )
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_text = tk.Label(
        frame,
        text=content,
        font=(font, font_size),
        fg=color,
        bg=background_color,
        justify="left",
        anchor="w",
        bd=0,
        relief="flat",
        wraplength=300,
        padx=PADDING,
        pady=PADDING,
    )
    label_text.place(relx=0, rely=0, anchor="nw", x=BORDER_WIDTH, y=BORDER_WIDTH)

    # Force geometry calculation
    top.update_idletasks()

    # Get requested size of label
    label_width = label_text.winfo_reqwidth()
    label_height = label_text.winfo_reqheight()

    # Set window size to label size + padding (10px on each side)
    window_width = label_width + BORDER_WIDTH * 2
    window_height = label_height + BORDER_WIDTH * 2
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
