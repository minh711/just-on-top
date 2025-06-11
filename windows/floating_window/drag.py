drag_data = {}

def start_drag(event, window):
    global drag_data
    drag_data = {'x': event.x, 'y': event.y}

def do_drag(event, window):
    x = window.winfo_x() - drag_data['x'] + event.x
    y = window.winfo_y() - drag_data['y'] + event.y
    window.geometry(f"+{x}+{y}")
