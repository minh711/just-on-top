from tkinter import colorchooser, Toplevel


def center_colorchooser_on_parent(parent):
    # Estimated size of the color chooser dialog (in pixels)
    dialog_width = 400
    dialog_height = 300

    # Create a temporary, invisible window as the parent of the dialog
    temp = Toplevel(parent)
    temp.withdraw()

    parent.update_idletasks()
    parent_x = parent.winfo_rootx()
    parent_y = parent.winfo_rooty()
    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()

    center_x = parent_x + (parent_width // 2) - (dialog_width // 2)
    center_y = parent_y + (parent_height // 2) - (dialog_height // 2)

    temp.geometry(f"+{center_x}+{center_y}")
    temp.update_idletasks()

    # Launch the color chooser with the temp window as the parent
    color = colorchooser.askcolor(parent=temp)[1]

    temp.destroy()
    return color


def update_color_text(label_text, root):
    color = center_colorchooser_on_parent(root)
    if color:
        label_text.configure(fg=color)


def update_color_background(label_text, root):
    color = center_colorchooser_on_parent(root)
    if color:
        label_text.configure(bg=color)
