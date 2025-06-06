from languages import languages

current_language = "English"

def set_language(language, reload_callback):
    from utils.file_ops import save_text
    global current_language
    confirm = save_text()
    if confirm:
        current_language = language
        reload_callback()
