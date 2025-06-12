import platform
import os
import customtkinter as ctk
from tkinter import (
    scrolledtext,
)  # No direct ctk replacement, can use CTkTextbox if scroll not needed
from windows.main_window.menu import setup_menu
from windows.main_window.controls import create_buttons
from utils.file_ops import resource_path, save_text
from utils.constants import SYMBOLS
from utils.settings import update_settings
from controls.text import update_text


def create_control_window(root, label_text, reload_window):
    def exit_application():
        confirm = save_text()
        if confirm:
            root.quit()
            root.destroy()

    control_window = ctk.CTkToplevel(root)
    control_window.title("Just On Top")
    control_window.protocol("WM_DELETE_WINDOW", exit_application)

    # --- Container Frame ---
    container = ctk.CTkFrame(control_window)
    container.pack(fill="both", expand=True, padx=10, pady=10)

    # --- Symbol Buttons ---
    symbol_frame = ctk.CTkFrame(container)
    symbol_frame.pack(fill="x", pady=(0, 10))

    def insert_symbol(symbol):
        text_area.insert("insert", symbol)
        update_text(text_area, label_text)

    symbols = SYMBOLS
    for sym in symbols:
        btn = ctk.CTkButton(
            master=symbol_frame,
            text=sym,
            font=("Helvetica", 12),
            command=lambda s=sym: insert_symbol(s),
            width=30,
        )
        btn.pack(side="left", padx=2)

    # --- Text Area ---
    text_area = ctk.CTkTextbox(
        master=container,
        width=400,
        height=160,
        font=("Helvetica", 12),
        wrap="word",
    )
    text_area.pack(fill="both", expand=True, pady=(0, 10))

    save_after_id = None

    def auto_save_text():
        content = text_area.get("1.0", "end-1c")
        update_settings({"content": content})

    def on_text_change(event=None):
        update_text(text_area, label_text)
        nonlocal save_after_id
        if save_after_id:
            control_window.after_cancel(save_after_id)
        save_after_id = control_window.after(500, auto_save_text)

    text_area.bind("<KeyRelease>", on_text_change)

    # --- Menu ---
    setup_menu(
        root, control_window, reload_window, text_area=text_area, label_text=label_text
    )

    # --- Buttons ---
    create_buttons(container, text_area, label_text)

    # --- Let window size to content ---
    control_window.update_idletasks()
    control_window.minsize(width=320, height=320)

    return control_window, text_area
