import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkfont
from models.settings import Settings
from utils.settings import load_settings, update_settings
from utils.constants import DEFAULT_FONT_SIZE, BORDER_WIDTH


def center_window_on_parent(window, parent, width, height):
    parent.update_idletasks()
    parent_x = parent.winfo_x()
    parent_y = parent.winfo_y()
    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()

    x = parent_x + int((parent_width / 2) - (width / 2))
    y = parent_y + int((parent_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")


def choose_font(parent, floating_window, label_text, text_area):
    def update_listbox(*_):
        typed = search_var.get().lower()
        for label in font_labels:
            font_name = label.cget("text").lower()
            if typed in font_name:
                if not getattr(label, "visible", False):
                    label.pack(fill="x", padx=5, pady=2)
                    label.visible = True
            else:
                if getattr(label, "visible", True):
                    label.pack_forget()
                    label.visible = False

    def on_select(font_name):
        selected_label.configure(
            text=f"Selected: {font_name}",
            font=ctk.CTkFont(family=font_name, weight="bold", size=14),
        )
        settings: Settings = load_settings()
        update_settings({"font": font_name})

        font_size = settings.get("font_size", DEFAULT_FONT_SIZE)
        label_text.configure(font=(font_name, font_size))
        text_area.configure(font=(font_name, font_size))
        floating_window.update_idletasks()

        label_width = label_text.winfo_reqwidth()
        label_height = label_text.winfo_reqheight()

        window_width = label_width + BORDER_WIDTH * 2
        window_height = label_height + BORDER_WIDTH * 2
        floating_window.winfo_toplevel().geometry(f"{window_width}x{window_height}")

    font_labels = []

    dialog = ctk.CTkToplevel()
    dialog.title("Choose Font")
    dialog.withdraw()
    center_window_on_parent(dialog, parent, 300, 400)

    def on_close():
        dialog.destroy()

    dialog.protocol("WM_DELETE_WINDOW", on_close)

    selected_label = ctk.CTkLabel(
        dialog, text="Selected: None", font=ctk.CTkFont(weight="bold")
    )
    selected_label.pack(pady=(10, 5))

    ctk.CTkLabel(dialog, text="Search font:").pack()

    search_var = ctk.StringVar()
    search_var.trace_add("write", update_listbox)
    search_entry = ctk.CTkEntry(
        dialog, textvariable=search_var, placeholder_text="Type to search..."
    )
    search_entry.pack(padx=10, pady=5, fill="x")

    scroll_frame = ctk.CTkScrollableFrame(dialog)
    scroll_frame.pack(padx=10, pady=10, fill="both", expand=True)

    all_fonts = sorted(tkfont.families())

    for font_name in all_fonts:
        label = ctk.CTkLabel(
            scroll_frame,
            text=font_name,
            font=(font_name, DEFAULT_FONT_SIZE),
            anchor="w",
            cursor="hand2",
        )
        label.bind("<Button-1>", lambda e, f=font_name: on_select(f))
        font_labels.append(label)

    update_listbox()

    def show_dialog():
        dialog.update_idletasks()
        dialog.deiconify()
        search_entry.focus()

    dialog.after_idle(show_dialog)
