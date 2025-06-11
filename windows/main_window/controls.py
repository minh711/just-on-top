import tkinter as tk
import controls.language as lang_module
from controls.text import update_text
from controls.color import update_color_text, update_color_background
from controls.font import adjust_font_size
from controls.window import toggle_window

def create_buttons(parent, text_area, label_text):
    # Dynamically fetch language each time in case it has changed
    lang = lang_module.current_language
    texts = lang_module.languages[lang]

    btn_data = [
        (texts["update_text"], lambda: update_text(text_area, label_text)),
        (texts["change_text_color"], lambda: update_color_text(label_text)),
        (texts["change_bg_color"], lambda: update_color_background(label_text)),
        (texts["adjust_font_size"], lambda: adjust_font_size(label_text)),
        (texts["toggle_text"], lambda: toggle_window(label_text.master))
    ]

    for text, cmd in btn_data:
        tk.Button(
            parent,
            text=text,
            command=cmd,
        ).pack(pady=5, padx=10, fill='x')
