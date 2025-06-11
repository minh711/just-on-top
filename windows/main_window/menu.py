from tkinter import Menu
import controls.language as lang_module
from windows.guide_window.guide_window import GuideWindow
from utils.file_ops import save_text
from utils.settings import save_settings

from controls.text import update_text
from controls.color import update_color_text, update_color_background
from controls.font import adjust_font_size
from controls.window import toggle_window
from controls.update_font import choose_font


def setup_menu(root, control_window, reload_window, text_area=None, label_text=None):
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
            label=texts["update_text"],
            command=lambda: update_text(text_area, label_text),
        )
        options_menu.add_command(
            label=texts["change_text_color"],
            command=lambda: update_color_text(label_text),
        )
        options_menu.add_command(
            label=texts["change_bg_color"],
            command=lambda: update_color_background(label_text),
        )
        options_menu.add_command(
            label=texts["adjust_font_size"],
            command=lambda: adjust_font_size(label_text),
        )
        options_menu.add_command(
            label=texts["toggle_text"], command=lambda: toggle_window(label_text.master)
        )
        options_menu.add_command(label="Change Font", command=choose_font)

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


def set_language(language, root, reload_window):
    confirm = save_text()
    if confirm:
        lang_module.current_language = language
        save_settings({"language": language})
        reload_window()
