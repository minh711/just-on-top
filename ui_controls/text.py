from .window import adjust_window_size

def update_text(text_area, label_text):
    new_text = text_area.get("1.0", 'end').strip()
    label_text.config(text=new_text)
    adjust_window_size(label_text)
