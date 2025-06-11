from typing import TypedDict

class Settings(TypedDict, total=False):
    language: str
    font_size: int
    content: str
    # Add other keys as needed, for example:
    # theme: str
    # font_size: int