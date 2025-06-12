import tkinter as tk
from tkinter import scrolledtext
from windows.main_window.menu import setup_menu
from windows.floating_window.drag import start_drag, do_drag
from windows.floating_window.floating_window import create_floating_window
from windows.main_window.main_window import create_control_window
from utils.file_ops import resource_path, save_text

top = control_window = label_text = text_area = None


def create_windows(root):
    global top, control_window, label_text, text_area

    top, label_text = create_floating_window(root)
    control_window, text_area = create_control_window(
        root, top, label_text, reload_window
    )


def exit_application(root):
    confirm = save_text()
    if confirm:
        root.quit()
        root.destroy()


def reload_window():
    global top, control_window
    top.destroy()
    control_window.destroy()
    create_windows(tk._default_root)
