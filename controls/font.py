import tkinter as tk
from tkinter import simpledialog
from controls.language import languages
from .window import adjust_window_size

current_language = "English"  # Sync with main app if it's dynamic


class FontSizeDialog(simpledialog.Dialog):
    def body(self, master):
        self.title(languages[current_language]["font_size_title"])
        self.iconbitmap("assets/jot_icon.ico")

        tk.Label(master, text=languages[current_language]["font_size_prompt"]).grid(
            row=0, column=0, padx=10, pady=10
        )
        self.input_var = tk.IntVar(value=12)
        self.spinbox = tk.Spinbox(
            master, from_=8, to=72, textvariable=self.input_var, width=5
        )
        self.spinbox.grid(row=1, column=0, padx=10, pady=5)
        return self.spinbox  # initial focus

    def apply(self):
        self.result = self.input_var.get()


def adjust_font_size(label_text):
    root = tk.Toplevel()
    root.withdraw()  # Optional: keep the root hidden if running inside a larger app
    dialog = FontSizeDialog(root)
    font_size = dialog.result
    root.destroy()

    if font_size:
        label_text.config(font=("Helvetica", font_size, "bold"))
        adjust_window_size(label_text)
