from appdirs import user_data_dir
import os
import json
from typing import cast
from utils.constants import APP_NAME, SETTINGS_FILE
from models.settings import Settings

def get_settings_path():
    dir_path = user_data_dir(APP_NAME)
    os.makedirs(dir_path, exist_ok=True)
    return os.path.join(dir_path, SETTINGS_FILE)

''' Full override settings '''
def save_settings(settings: Settings):
    path = get_settings_path()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)

''' Update one or more settings without overwriting the rest. '''
def update_settings(partial: Settings):
    settings = load_settings()
    settings.update(partial)
    save_settings(settings)

def load_settings() -> Settings:
    path = get_settings_path()
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return cast(Settings, json.load(f))
    return {}
