import tkinter as tk
from tkinter import font


def choose_font():
    def update_listbox(event=None):
        typed = search_var.get().lower()
        listbox.delete(0, tk.END)
        for f in all_fonts:
            if typed in f.lower():
                listbox.insert(tk.END, f)

    def on_select(event=None):
        try:
            selection = listbox.get(listbox.curselection())
            print("Selected font:", selection)
            dialog.destroy()
        except tk.TclError:
            pass  # No selection made

    root = tk.Tk()
    root.withdraw()

    dialog = tk.Toplevel()
    dialog.title("Choose Font")
    dialog.geometry("300x400")
    dialog.grab_set()

    tk.Label(dialog, text="Search font:").pack(pady=(10, 0))

    search_var = tk.StringVar()
    search_entry = tk.Entry(dialog, textvariable=search_var)
    search_entry.pack(padx=10, fill=tk.X)
    search_entry.bind("<KeyRelease>", update_listbox)

    listbox = tk.Listbox(dialog)
    listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    listbox.bind("<Double-1>", on_select)
    listbox.bind("<Return>", on_select)

    all_fonts = sorted(font.families())
    for f in all_fonts:
        listbox.insert(tk.END, f)

    tk.Button(dialog, text="OK", command=on_select).pack(pady=5)

    search_entry.focus()
    dialog.mainloop()
