def adjust_window_size(label_text):
    label_text.update_idletasks()
    width = max(label_text.winfo_width() + 40, 300)
    height = label_text.winfo_height() + 40
    label_text.master.geometry(f"{width}x{height}")
    label_text.config(wraplength=width - 40)

def toggle_window(top):
    if top.winfo_viewable():
        top.withdraw()
    else:
        top.deiconify()
