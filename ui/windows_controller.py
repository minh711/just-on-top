import tkinter as tk
from tkinter import scrolledtext
from ui.menu import setup_menu
from ui.drag import start_drag, do_drag
from ui.controls import create_buttons
from ui.windows.floating import create_floating_window
from ui.windows.control import create_control_window
from utils.file_ops import resource_path, save_text

top = control_window = label_text = text_area = None

def create_windows(root):
    global top, control_window, label_text, text_area

    top, label_text = create_floating_window(root)
    control_window, text_area = create_control_window(root, label_text, reload_window)

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
