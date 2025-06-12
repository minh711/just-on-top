import customtkinter as ctk
import tkinter as tk
from controls.language import languages
from .window import adjust_window_size

current_language = "English"  # Sync with main app if it's dynamic


def center_window_on_parent(window, parent, width, height):
    parent.update_idletasks()
    parent_x = parent.winfo_x()
    parent_y = parent.winfo_y()
    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()

    x = parent_x + int((parent_width / 2) - (width / 2))
    y = parent_y + int((parent_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")


def adjust_font_size(parent, label_text):
    def on_confirm():
        try:
            font_size = int(spinbox.get())
            if font_size:
                label_text.configure(font=("Helvetica", font_size, "bold"))
                adjust_window_size(label_text)
        except ValueError:
            pass
        dialog.destroy()

    dialog = ctk.CTkToplevel()
    dialog.withdraw()
    dialog.title(languages[current_language]["font_size_title"])
    dialog.resizable(False, False)
    center_window_on_parent(dialog, parent, 260, 150)
    dialog.grab_set()

    ctk.CTkLabel(dialog, text=languages[current_language]["font_size_prompt"]).pack(
        padx=20, pady=(15, 5)
    )

    spinbox = ctk.CTkEntry(dialog, width=60)
    spinbox.insert(0, "12")
    spinbox.pack(pady=(0, 10))

    button = ctk.CTkButton(dialog, text="OK", command=on_confirm)
    button.pack(pady=(0, 15))

    def show_dialog():
        dialog.update_idletasks()
        dialog.deiconify()
        spinbox.focus()

    dialog.after(200, show_dialog)  # Wait a little for smooth showing
