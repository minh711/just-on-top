import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkfont


def choose_font():
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
