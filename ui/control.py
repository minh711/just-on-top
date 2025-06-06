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
    control_window.geometry("360x300")
    control_window.configure(bg='#F0F0F0')
    control_window.protocol("WM_DELETE_WINDOW", exit_application)

    setup_menu(root, control_window, reload_window)

    text_area = scrolledtext.ScrolledText(
        control_window,
        width=36,
        height=5,
        bg='#FFFFFF',
        fg='black',
        font=('Helvetica', 12)
    )
    text_area.pack(pady=10, padx=10)

    create_buttons(control_window, text_area, label_text)

    icon_path = resource_path('assets/jot_icon.ico')
    control_window.iconbitmap(icon_path)

    return control_window, text_area
