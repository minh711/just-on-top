import tkinter as tk
from ui.language import languages, current_language
from ui_controls import update_text, update_color_text, update_color_background, adjust_font_size, toggle_window

def create_buttons(parent, text_area, label_text):
    btn_data = [
        (languages[current_language]["update_text"], lambda: update_text(text_area, label_text)),
        (languages[current_language]["change_text_color"], lambda: update_color_text(label_text)),
        (languages[current_language]["change_bg_color"], lambda: update_color_background(label_text)),
        (languages[current_language]["adjust_font_size"], lambda: adjust_font_size(label_text)),
        (languages[current_language]["toggle_text"], lambda: toggle_window(label_text.master))
    ]
    for text, cmd in btn_data:
        tk.Button(parent, text=text, command=cmd).pack(pady=5, padx=10, fill='x')
