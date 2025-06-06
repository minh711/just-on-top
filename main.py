import tkinter as tk
from ui.windows import create_windows

def main():
    root = tk.Tk()
    root.withdraw()
    create_windows(root)
    root.mainloop()

if __name__ == "__main__":
    main()
