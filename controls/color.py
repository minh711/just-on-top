from tkinter import colorchooser, Toplevel
from utils.settings import update_settings


def update_color_text(label_text, root):
    color = colorchooser.askcolor(parent=root)[1]
    if color:
        label_text.configure(fg=color)
        update_settings({"color": color})


def update_color_background(label_text, root, floating_window):
    color = colorchooser.askcolor(parent=root)[1]
    if color:
        label_text.configure(bg=color)
        floating_window.configure(bg=color)
        update_settings({"background_color": color})
