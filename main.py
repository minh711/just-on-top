import os
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import datetime
from ui_controls import update_text, update_color_text, update_color_background, adjust_font_size, toggle_window
from languages import languages
from guide import GuideWindow

default_font = "SVN-Comic Sans MS"

current_language = "English"

def resource_path(relative_path):
    """ Get path to resource during execution """
    return os.path.join(os.path.dirname(__file__), relative_path)

def start_drag(event):
    global drag_data
    drag_data = {'x': event.x, 'y': event.y}

def do_drag(event):
    x = top.winfo_x() - drag_data['x'] + event.x
    y = top.winfo_y() - drag_data['y'] + event.y
    top.geometry(f"+{x}+{y}")

def save_text():
    text = text_area.get("1.0", tk.END).strip()
    if text:
        default_filename = f"jot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        confirm = messagebox.askyesnocancel(
            "Save Confirmation", 
            languages[current_language]["save_confirmation"]
        )
        if confirm:  # User clicked "Yes"
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                initialfile=default_filename,
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
            if file_path:  # Only if the user selects a file
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(text)
                return True
            else:
                return None  # User closed the save dialog
        elif confirm is False:  # User clicked "No"
            return True
        else:  # User clicked "Cancel"
            return None
    return True

def exit_application():
    confirm = save_text()
    if confirm:
        root.quit()
        root.destroy()

def create_windows():
    global top, control_window, label_text, text_area, guide_window

    top = tk.Toplevel(root)
    top.attributes('-topmost', True)
    top.overrideredirect(True)
    top.wm_attributes('-transparentcolor', top['bg'])

    label_text = tk.Label(
        top,
        text="Your text here",
        font=(default_font, 12, 'bold'),
        fg='white',
        bg='#4A90E2',
        padx=10,
        pady=4,
        justify='left',
        anchor='e',
        bd=2,
        relief='solid',
        highlightbackground='#4A90E2',
        highlightthickness=1,
        wraplength=800
    )
    label_text.place(relx=1, rely=0, anchor='ne', x=-10, y=10)

    top.bind("<ButtonPress-1>", lambda event: start_drag(event))
    top.bind("<B1-Motion>", lambda event: do_drag(event))

    control_window = tk.Toplevel(root)
    control_window.title("Just On Top")
    control_window.geometry("360x320")
    control_window.configure(bg='#F0F0F0')
    control_window.protocol("WM_DELETE_WINDOW", exit_application)

    menu_bar = tk.Menu(control_window)
    control_window.config(menu=menu_bar)

    options_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label=languages[current_language]["options"], menu=options_menu)

    language_menu = tk.Menu(options_menu, tearoff=0)
    options_menu.add_cascade(label=languages[current_language]["language"], menu=language_menu)

    for lang in languages.keys():
        language_menu.add_command(label=lang, command=lambda l=lang: set_language(l))

    text_area = scrolledtext.ScrolledText(control_window, width=36, height=5, bg='#FFFFFF', fg='black', font=(default_font, 12))
    text_area.pack(pady=10, padx=10)

    create_buttons(control_window)

    help_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label=languages[current_language]["help"], menu=help_menu)
    help_menu.add_command(label=languages[current_language]["guide"], command=lambda: guide_window.toggle())

    guide_window = GuideWindow(root, languages, current_language)
    
    icon_path = resource_path('jot_icon.ico')
    control_window.iconbitmap(icon_path)

def create_buttons(control_window):
    global buttons

    buttons = []
    btn_update_text = tk.Button(control_window, text=languages[current_language]["update_text"], command=lambda: update_text(text_area, label_text))
    btn_update_text.pack(pady=5, padx=10, fill='x')
    buttons.append(btn_update_text)

    btn_update_color_text = tk.Button(control_window, text=languages[current_language]["change_text_color"], command=lambda: update_color_text(label_text))
    btn_update_color_text.pack(pady=5, padx=10, fill='x')
    buttons.append(btn_update_color_text)

    btn_update_color_bg = tk.Button(control_window, text=languages[current_language]["change_bg_color"], command=lambda: update_color_background(label_text))
    btn_update_color_bg.pack(pady=5, padx=10, fill='x')
    buttons.append(btn_update_color_bg)

    btn_adjust_font_size = tk.Button(control_window, text=languages[current_language]["adjust_font_size"], command=lambda: adjust_font_size(label_text))
    btn_adjust_font_size.pack(pady=5, padx=10, fill='x')
    buttons.append(btn_adjust_font_size)

    btn_toggle_window = tk.Button(control_window, text=languages[current_language]["toggle_text"], command=lambda: toggle_window(top))
    btn_toggle_window.pack(pady=5, padx=10, fill='x')
    buttons.append(btn_toggle_window)

def reload_window():
    top.destroy()
    control_window.destroy()
    create_windows()
    
def set_language(language):
    global current_language
    confirm = save_text()
    if confirm:
        current_language = language
        reload_window()

root = tk.Tk()
root.withdraw()
create_windows()

root.mainloop()
