from tkinter import Menu
import controls.language as lang_module
from windows.guide_window.guide_window import GuideWindow
from utils.file_ops import save_text
from utils.settings import update_settings

from controls.text import update_text
from controls.color import update_color_text, update_color_background
from controls.font import adjust_font_size
from controls.update_font import choose_font
from tkinter import messagebox


def setup_menu(
    root,
    control_window,
    floating_window,
    reload_window,
    text_area=None,
    label_text=None,
):
    menu_bar = Menu(control_window)
    control_window.config(menu=menu_bar)

    lang = lang_module.current_language
    texts = lang_module.languages[lang]

    # Options
    options_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label=texts["options"], menu=options_menu)

    # --- Move control actions to Options menu ---
    if text_area and label_text:
        options_menu.add_command(
            label=texts["change_text_color"],
            command=lambda: update_color_text(label_text, control_window),
        )

        options_menu.add_command(
            label=texts["change_bg_color"],
            command=lambda: update_color_background(
                label_text, control_window, floating_window
            ),
        )

        options_menu.add_command(
            label="Toggle Bordered",
            command=lambda: toggle_bordered(reload_window),
        )

        options_menu.add_command(
            label=texts["adjust_font_size"],
            command=lambda: adjust_font_size(control_window, label_text, text_area),
        )

        options_menu.add_command(
            label="Change font",
            command=lambda: choose_font(
                control_window, floating_window, label_text, text_area
            ),
        )

    # Language Submenu
    language_menu = Menu(options_menu, tearoff=0)
    options_menu.add_cascade(label=texts["language"], menu=language_menu)

    for language in lang_module.languages:
        language_menu.add_command(
            label=language,
            command=lambda l=language: set_language(l, root, reload_window),
        )

    # Help
    guide_window = GuideWindow(root, lang_module.languages, lang)
    help_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label=texts["help"], menu=help_menu)

    help_menu.add_command(label=texts["guide"], command=guide_window.toggle)

    # Cautions* menu
    caution_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Cautions*", menu=caution_menu)
    caution_menu.add_command(
        label="About Font Selection",
        command=lambda: messagebox.showinfo(
            "Font Selection Caution",
            "Loading system fonts may cause lag.\n\n"
            "It may take time to open or close the font dialog, "
            "and resizing the font selection window can also cause temporary performance issues.\n\n"
            "We recommend using this feature sparingly.\n\n"
            "Thank you for your understanding!",
        ),
    )


def set_language(language, root, reload_window):
    confirm = save_text()
    if confirm:
        lang_module.current_language = language
        update_settings({"language": language})
        reload_window()


def toggle_bordered(reload_window):
    from utils.settings import load_settings

    settings = load_settings()
    current = settings.get("bordered", 1)
    new_value = 0 if current else 1
    update_settings({"bordered": new_value})
    reload_window()
