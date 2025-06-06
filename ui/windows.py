import tkinter as tk
from tkinter import scrolledtext, Menu
from ui.controls import create_buttons
from ui.guide import GuideWindow
from ui.language import languages, current_language, set_language
from utils.file_ops import resource_path, save_text

top = control_window = label_text = text_area = guide_window = None
drag_data = {}

def start_drag(event):
    global drag_data
    drag_data = {'x': event.x, 'y': event.y}

def do_drag(event):
    x = top.winfo_x() - drag_data['x'] + event.x
    y = top.winfo_y() - drag_data['y'] + event.y
    top.geometry(f"+{x}+{y}")

def create_windows(root):
    global top, control_window, label_text, text_area, guide_window

    # Floating top window
    top = tk.Toplevel(root)
    top.attributes('-topmost', True)
    top.overrideredirect(True)
    top.wm_attributes('-transparentcolor', top['bg'])

    label_text = tk.Label(
        top,
        text="Your text here",
        font=('Helvetica', 12, 'bold'),
        fg='white',
        bg='#4A90E2',
        padx=20,
        pady=10,
        justify='left',
        anchor='e',
        bd=2,
        relief='solid',
        highlightbackground='#4A90E2',
        highlightthickness=1,
        wraplength=300
    )
    label_text.place(relx=1, rely=0, anchor='ne', x=-10, y=10)

    top.bind("<ButtonPress-1>", start_drag)
    top.bind("<B1-Motion>", do_drag)

    # Control panel window
    control_window = tk.Toplevel(root)
    control_window.title("Just On Top")
    control_window.geometry("360x300")
    control_window.configure(bg='#F0F0F0')
    control_window.protocol("WM_DELETE_WINDOW", lambda: exit_application(root))

    # Menu
    menu_bar = Menu(control_window)
    control_window.config(menu=menu_bar)

    options_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label=languages[current_language]["options"], menu=options_menu)

    language_menu = Menu(options_menu, tearoff=0)
    options_menu.add_cascade(label=languages[current_language]["language"], menu=language_menu)
    for lang in languages.keys():
        language_menu.add_command(label=lang, command=lambda l=lang: set_language(l, root))

    help_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label=languages[current_language]["help"], menu=help_menu)

    guide_window = GuideWindow(root, languages, current_language)
    help_menu.add_command(label=languages[current_language]["guide"], command=guide_window.toggle)

    # Text area
    text_area = scrolledtext.ScrolledText(control_window, width=36, height=5, bg='#FFFFFF', fg='black', font=('Helvetica', 12))
    text_area.pack(pady=10, padx=10)

    # Buttons
    create_buttons(control_window, text_area, label_text)

    # Icon
    icon_path = resource_path('assets/jot_icon.ico')
    control_window.iconbitmap(icon_path)

def exit_application(root):
    confirm = save_text()
    if confirm:
        root.quit()
        root.destroy()

def reload_window(root):
    top.destroy()
    control_window.destroy()
    create_windows(root)

def set_language(language, root):
    from ui.language import current_language  # make sure to update reference
    confirm = save_text()
    if confirm:
        # Must update current_language this way if it's being shared globally
        import ui.language as lang_module
        lang_module.current_language = language
        reload_window(root)
