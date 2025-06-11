from tkinter import simpledialog
from controls.language import languages
from .window import adjust_window_size

current_language = "English"  # Make sure to sync with main app if it's dynamic

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
