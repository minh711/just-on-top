from appdirs import user_data_dir
import os
import json

APP_NAME = "JustOnTop"
SETTINGS_FILE = "settings.json"

def get_settings_path():
    dir_path = user_data_dir(APP_NAME)
    os.makedirs(dir_path, exist_ok=True)
    return os.path.join(dir_path, SETTINGS_FILE)

def save_settings(settings):
    path = get_settings_path()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)

def load_settings():
    path = get_settings_path()
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
