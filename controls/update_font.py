import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkfont


def center_window_on_parent(window, parent, width, height):
    parent.update_idletasks()
    parent_x = parent.winfo_x()
    parent_y = parent.winfo_y()
    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()

    x = parent_x + int((parent_width / 2) - (width / 2))
    y = parent_y + int((parent_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")


# Cache fonts once to avoid repeated delays
def get_cached_fonts():
    if not hasattr(get_cached_fonts, "fonts"):
        preload_root = tk.Tk()
        preload_root.withdraw()
        preload_root.update_idletasks()
        get_cached_fonts.fonts = sorted(tkfont.families(preload_root))
        preload_root.destroy()
    return get_cached_fonts.fonts


def choose_font(parent):
    def update_listbox(*_):
        typed = search_var.get().lower()
        for label in font_labels:
            label.pack_forget()
        for label in font_labels:
            if typed in label.cget("text").lower():
                label.pack(fill="x", padx=5, pady=2)

    def on_select(font_name):
        selected_label.configure(
            text=f"Selected: {font_name}",
            font=ctk.CTkFont(family=font_name, weight="bold", size=14),
        )
        print("Selected font:", font_name)

    font_labels = []

    dialog = ctk.CTkToplevel()
    dialog.withdraw()
    dialog.title("Choose Font")
    dialog.grab_set()
    center_window_on_parent(dialog, parent, 300, 400)

    def on_close():
        dialog.grab_release()
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

    # Get fonts (cached)
    all_fonts = get_cached_fonts()

    for font_name in all_fonts:
        label = ctk.CTkLabel(
            scroll_frame,
            text=font_name,
            anchor="w",
            cursor="hand2",
            # Do NOT apply font preview here to speed up
        )
        label.bind("<Button-1>", lambda e, f=font_name: on_select(f))
        font_labels.append(label)

    update_listbox()

    def show_dialog():
        dialog.update_idletasks()
        dialog.deiconify()
        search_entry.focus()

    dialog.after_idle(show_dialog)


# Example usage
if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("400x200")
    root.title("Font Chooser Test")

    button = ctk.CTkButton(root, text="Choose Font", command=lambda: choose_font(root))
    button.pack(pady=50)

    root.mainloop()
