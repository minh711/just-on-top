from utils.constants import PADDING


def adjust_window_size(label_text):
    label_text.config(wraplength=300)
    label_text.update_idletasks()

    label_width = label_text.winfo_reqwidth()
    label_height = label_text.winfo_reqheight()

    window_width = label_width + PADDING * 2
    window_height = label_height + PADDING * 2

    label_text.master.geometry(f"{window_width}x{window_height}")


def toggle_window(top):
    if top.winfo_viewable():
        top.withdraw()
    else:
        top.deiconify()
