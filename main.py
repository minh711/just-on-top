# Import the tkinter module for GUI components
import tkinter as tk
from windows.windows_controller import create_windows

# Main function to start the application
def main():
    # Create the main hidden root window (required by tkinter)
    root = tk.Tk()
    root.withdraw()  # Hide the root window since we use custom windows

    # Create custom floating and control windows
    create_windows(root)

    # Start the tkinter event loop to keep the app running
    root.mainloop()

if __name__ == "__main__":
    main()
