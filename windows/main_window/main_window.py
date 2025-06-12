import platform
import os
import customtkinter as ctk
from tkinter import scrolledtext  # Still no CTk replacement with scrollbar
from windows.main_window.menu import setup_menu
from utils.file_ops import resource_path, save_text
from utils.constants import SYMBOLS
from utils.settings import update_settings
from controls.text import update_text
import controls.language as lang_module
from controls.window import toggle_window


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")


def create_control_window(root, label_text, reload_window):
    # Languages
    lang = lang_module.current_language
    texts = lang_module.languages[lang]

    def exit_application():
        if save_text():
            root.quit()
            root.destroy()

    control_window = ctk.CTkToplevel(root)
    control_window.title("Just On Top")
    control_window.protocol("WM_DELETE_WINDOW", exit_application)

    # Container frame
    container = ctk.CTkFrame(control_window)
    container.pack(fill="both", expand=True, padx=10, pady=10)

    # ===================== Symbols =====================
    symbol_frame = ctk.CTkFrame(container)
    symbol_frame.pack(fill="x", pady=(0, 10))

    def insert_symbol(symbol):
        text_area.insert("insert", symbol)
        update_text(text_area, label_text)

    for sym in SYMBOLS:
        ctk.CTkButton(
            master=symbol_frame,
            text=sym,
            font=("Helvetica", 12),
            command=lambda s=sym: insert_symbol(s),
            width=30,
        ).pack(side="left", padx=2)
    # ===================== End symbols =====================

    # ===================== Text area =====================
    text_area = ctk.CTkTextbox(
        master=container,
        width=400,
        height=160,
        font=("Helvetica", 16),
        wrap="word",
    )
    text_area.pack(fill="both", expand=True, pady=(0, 10))

    save_after_id = None

    def auto_save_text():
        content = text_area.get("1.0", "end-1c")
        update_settings({"content": content})

    def on_text_change(event=None):
        nonlocal save_after_id
        update_text(text_area, label_text)
        if save_after_id:
            control_window.after_cancel(save_after_id)
        save_after_id = control_window.after(500, auto_save_text)

    text_area.bind("<KeyRelease>", on_text_change)
    # ===================== End text area =====================

    # Menu
    setup_menu(
        root, control_window, reload_window, text_area=text_area, label_text=label_text
    )

    # Toggle Label Window Button
    ctk.CTkButton(
        master=container,
        text=texts["toggle_text"],
        command=lambda: toggle_window(label_text.master),
    ).pack(pady=5, padx=10, fill="x")

    # Final Layout Adjustments
    control_window.update_idletasks()
    control_window.minsize(width=440, height=440)
    center_window(control_window, 440, 440)

    return control_window, text_area
