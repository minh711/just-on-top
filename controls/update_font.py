import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkfont


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")


def center_window_on_parent(window, parent, width, height):
    parent.update_idletasks()  # Make sure geometry info is up-to-date

    parent_x = parent.winfo_x()
    parent_y = parent.winfo_y()
    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()

    x = parent_x + int((parent_width / 2) - (width / 2))
    y = parent_y + int((parent_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")


def choose_font(parent):
    def update_listbox(*_):
        typed = search_var.get().lower()
        for label in font_labels:
            label.pack_forget()
        for label in font_labels:
            if typed in label.cget("text").lower():
                label.pack(fill="x", padx=5, pady=2)

    def on_select(font_name):
        print("Selected font:", font_name)
        dialog.destroy()

    # Preload fonts
    preload_root = tk.Tk()
    preload_root.withdraw()
    preload_root.update_idletasks()
    all_fonts = sorted(tkfont.families(preload_root))
    preload_root.destroy()

    font_labels = []

    # Create hidden dialog
    dialog = ctk.CTkToplevel()
    dialog.withdraw()
    dialog.title("Choose Font")
    dialog.geometry("300x400")
    # center_window(dialog, 300, 400)
    center_window_on_parent(dialog, parent, 300, 400)

    dialog.grab_set()

    ctk.CTkLabel(dialog, text="Search font:").pack(pady=(10, 0))

    search_var = ctk.StringVar()
    search_entry = ctk.CTkEntry(
        dialog, textvariable=search_var, placeholder_text="Type to search..."
    )
    search_entry.pack(padx=10, pady=5, fill="x")

    scroll_frame = ctk.CTkScrollableFrame(dialog)
    scroll_frame.pack(padx=10, pady=10, fill="both", expand=True)

    for font_name in all_fonts:
        label = ctk.CTkLabel(scroll_frame, text=font_name, anchor="w", cursor="hand2")
        label.bind("<Button-1>", lambda e, f=font_name: on_select(f))
        font_labels.append(label)

    update_listbox()

    def show_dialog():
        dialog.update_idletasks()  # Ensure layout is flushed
        dialog.deiconify()  # Show the fully rendered dialog
        search_entry.focus()

    # Wait until all UI work is queued, then show
    dialog.after_idle(show_dialog)
