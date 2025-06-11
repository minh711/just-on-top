import os
import datetime
from tkinter import filedialog, messagebox
from controls.language import current_language
from controls.language import languages

def resource_path(relative_path):
    return os.path.join(os.path.dirname(__file__), '..', relative_path)

def save_text(text_area=None):
    if not text_area:
        return True
    text = text_area.get("1.0", "end").strip()
    if text:
        default_filename = f"jot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        confirm = messagebox.askyesnocancel(
            "Save Confirmation", 
            languages[current_language]["save_confirmation"]
        )
        if confirm:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                initialfile=default_filename,
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
            if file_path:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(text)
                return True
            else:
                return None
        elif confirm is False:
            return True
        else:
            return None
    return True
