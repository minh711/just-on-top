import platform
import tkinter as tk
from tkinter import scrolledtext
from ui.menu import setup_menu
from ui.controls import create_buttons
from utils.file_ops import resource_path, save_text

def create_control_window(root, label_text, reload_window):
    def exit_application():
        confirm = save_text()
        if confirm:
            root.quit()
            root.destroy()

    control_window = tk.Toplevel(root)
    control_window.title("Just On Top")
    control_window.configure(bg='#F0F0F0')
    control_window.protocol("WM_DELETE_WINDOW", exit_application)

    setup_menu(root, control_window, reload_window)

    # --- Container Frame ---
    container = tk.Frame(control_window, bg='#F0F0F0')
    container.pack(fill='both', expand=True, padx=10, pady=10)

    # --- Symbol Buttons ---
    symbol_frame = tk.Frame(container, bg='#F0F0F0')
    symbol_frame.pack(fill='x', pady=(0, 10))

    def insert_symbol(symbol):
        text_area.insert('insert', symbol)

    symbols = ['🟨', '✅', '❌', '⚠️', '🔥', '💡']
    for sym in symbols:
        btn = tk.Button(
            symbol_frame,
            text=sym,
            font=('Helvetica', 12),
            command=lambda s=sym: insert_symbol(s),
            width=3
        )
        btn.pack(side='left', padx=2)

    # --- Text Area ---
    text_area = scrolledtext.ScrolledText(
        container,
        width=36,
        height=5,
        bg='#FFFFFF',
        fg='black',
        font=('Helvetica', 12)
    )
    text_area.pack(fill='both', expand=True, pady=(0, 10))

    # --- Buttons ---
    create_buttons(container, text_area, label_text)

    # --- Set icon ---
    if platform.system() == "Windows":
        icon_path = resource_path('assets/jot_icon.ico')
        control_window.iconbitmap(icon_path)

    # --- Let window size to content ---
    control_window.update_idletasks()
    control_window.geometry("")  # Let Tkinter fit the window to its content

    return control_window, text_area
