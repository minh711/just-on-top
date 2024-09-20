from tkinter import colorchooser, simpledialog
from languages import languages

current_language = "English"

def update_text(text_area, label_text):
    new_text = text_area.get("1.0", 'end').strip()
    label_text.config(text=new_text)
    adjust_window_size(label_text)

def adjust_window_size(label_text):
    label_text.update_idletasks()
    width = max(label_text.winfo_width() + 40, 300)
    height = label_text.winfo_height() + 40
    label_text.master.geometry(f"{width}x{height}")
    label_text.config(wraplength=width - 40)

def update_color_text(label_text):
    color = colorchooser.askcolor()[1]
    if color:
        label_text.config(fg=color)

def update_color_background(label_text):
    color = colorchooser.askcolor()[1]
    if color:
        label_text.config(bg=color)

def adjust_font_size(label_text):
    font_size = simpledialog.askinteger(
        languages[current_language]["font_size_title"],
        languages[current_language]["font_size_prompt"],
        minvalue=8,
        maxvalue=72
    )
    if font_size:
        label_text.config(font=('Helvetica', font_size, 'bold'))
    adjust_window_size(label_text)

def toggle_window(top):
    if top.winfo_viewable():
        top.withdraw()
    else:
        top.deiconify()
