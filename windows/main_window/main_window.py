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
from windows.main_window.settings_panel import build_settings_frame


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

    # ===================== Settings toggle =====================
    settings_frame = build_settings_frame(container)

    def toggle_settings():
        if settings_frame.winfo_ismapped():
            settings_frame.pack_forget()
            control_window.minsize(width=440, height=440)
        else:
            settings_frame.pack(after=symbol_frame, fill="x", pady=(0, 10))
            control_window.minsize(width=440, height=600)

        control_window.update_idletasks()
        control_window.geometry(
            f"{control_window.winfo_reqwidth()}x{control_window.winfo_reqheight()}"
        )

    ctk.CTkButton(
        master=symbol_frame,
        text="Settings",
        command=toggle_settings,
        width=80,
    ).pack(side="right")
    # ===================== End settings toggle =====================

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

    return control_window, text_area
