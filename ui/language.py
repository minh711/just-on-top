from languages.languages import languages
from utils.settings import load_settings  # import settings loader

# Load the saved language from disk (fallback to English)
current_language = load_settings().get("language", "English")

def set_language(language, root, reload_window):
    from utils.file_ops import save_text
    from utils.settings import save_settings
    import ui.language as lang_module

    confirm = save_text()
    if confirm:
        lang_module.current_language = language
        save_settings({"language": language})  # persist it
        print(f"Language switched to: {language}")
        reload_window(root)
