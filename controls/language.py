from languages.languages import languages
from utils.settings import load_settings, save_settings
from models.settings import Settings
from utils.constants import DEFAULT_LANGUAGE

# Load the saved language from disk (fallback to English)
settings: Settings = load_settings()
current_language: str = settings.get("language", DEFAULT_LANGUAGE)


def set_language(language: str, root, reload_window):
    from utils.file_ops import save_text
    import controls.language as lang_module

    confirm = save_text()
    if confirm:
        lang_module.current_language = language
        new_settings: Settings = {"language": language}
        save_settings(new_settings)
        reload_window(root)
