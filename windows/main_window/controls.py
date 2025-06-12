import customtkinter as ctk
import controls.language as lang_module
from controls.text import update_text
from controls.color import update_color_text, update_color_background
from controls.font import adjust_font_size
from controls.window import toggle_window
from controls.update_font import choose_font


def create_buttons(parent, text_area, label_text):
    # Dynamically fetch language each time in case it has changed
    lang = lang_module.current_language
    texts = lang_module.languages[lang]

    btn_data = [
        (texts["toggle_text"], lambda: toggle_window(label_text.master)),
    ]

    for text, cmd in btn_data:
        ctk.CTkButton(
            master=parent,
            text=text,
            command=cmd,
        ).pack(pady=5, padx=10, fill="x")
