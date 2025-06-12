import customtkinter as ctk
from customtkinter import CTkInputDialog
from controls.language import languages
from .window import adjust_window_size

current_language = "English"  # Make sure to sync with main app if it's dynamic


def adjust_font_size(label_widget, parent_window):
    # Create the input dialog
    dialog = CTkInputDialog(
        title=languages[current_language]["font_size_title"],
        text=languages[current_language]["font_size_prompt"],
    )

    # Force the dialog to stay on top of the parent window
    dialog.lift()  # Bring to front
    dialog.wm_transient(parent_window)  # Set dialog as transient to the parent
    dialog.grab_set()  # Modal behavior (optional, prevents interaction with other windows)

    # Get the input after the dialog is shown
    input_str = dialog.get_input()

    if input_str:
        try:
            font_size = int(input_str)
            if 8 <= font_size <= 72:
                label_widget.configure(
                    font=ctk.CTkFont(family="Helvetica", size=font_size, weight="bold")
                )
        except ValueError:
            pass  # Optionally add error handling or a popup

    adjust_window_size(label_widget)
