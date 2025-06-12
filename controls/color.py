from tkinter import colorchooser, Toplevel


def update_color_text(label_text, root):
    color = colorchooser.askcolor(parent=root)[1]
    if color:
        label_text.configure(fg=color)


def update_color_background(label_text, root):
    color = colorchooser.askcolor(parent=root)[1]
    if color:
        label_text.configure(bg=color)
