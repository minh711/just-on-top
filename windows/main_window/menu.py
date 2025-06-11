from tkinter import Menu
import controls.language as lang_module
from windows.guide_window.guide_window import GuideWindow
from utils.file_ops import save_text
from utils.settings import save_settings

def setup_menu(root, control_window, reload_window):
    menu_bar = Menu(control_window)
    control_window.config(menu=menu_bar)

    lang = lang_module.current_language
    texts = lang_module.languages[lang]

    # Options
    options_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label=texts["options"], menu=options_menu)

    # Language Submenu
    language_menu = Menu(options_menu, tearoff=0)
    options_menu.add_cascade(label=texts["language"], menu=language_menu)

    for language in lang_module.languages:
        language_menu.add_command(
            label=language,
            command=lambda l=language: set_language(l, root, reload_window)
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
        save_settings({"language": language})  # Save to disk
        reload_window()
