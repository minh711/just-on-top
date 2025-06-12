# Import the tkinter module for GUI components
# import tkinter as tk
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import customtkinter as ctk
import tkinter as tk
from windows.windows_controller import create_windows


def resource_path(relative_path):
    """Get path to resource during execution"""
    return os.path.join(os.path.dirname(__file__), relative_path)


# Main function to start the application
def main():
    ctk.set_appearance_mode("Light")  # or "Dark"
    ctk.set_default_color_theme(resource_path("themes/light_theme.json"))

    # Create the main hidden root window (required by tkinter)
    root = ctk.CTk()
    root.withdraw()  # Hide the root window since we use custom windows

    # Create custom floating and control windows
    create_windows(root)

    # Start the tkinter event loop to keep the app running
    root.mainloop()


if __name__ == "__main__":
    main()
