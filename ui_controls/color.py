from tkinter import colorchooser

def update_color_text(label_text):
    color = colorchooser.askcolor()[1]
    if color:
        label_text.config(fg=color)

def update_color_background(label_text):
    color = colorchooser.askcolor()[1]
    if color:
        label_text.config(bg=color)
