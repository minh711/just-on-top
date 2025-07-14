from typing import TypedDict


class Settings(TypedDict, total=False):
    language: str
    content: str
    font: str
    font_size: int
    color: str
    background_color: str
    bordered: int
