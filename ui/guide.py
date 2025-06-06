import tkinter as tk

class GuideWindow:
    def __init__(self, root, languages, current_language):
        self.root = root
        self.languages = languages
        self.current_language = current_language
        self.guide_window = None
        self.create_window()

    def create_window(self):
        self.guide_window = tk.Toplevel(self.root)
        self.guide_window.title("Guide")
        self.guide_window.geometry("360x400")
        self.guide_window.configure(bg='#F0F0F0')
        self.guide_window.withdraw()

        self.guide_label = tk.Label(
            self.guide_window,
            text=self.languages[self.current_language]["guide_text"],
            bg='#F0F0F0',
            fg='black',
            font=('Helvetica', 12),
            justify='left',
            anchor='w',
            wraplength=300
        )
        self.guide_label.pack(pady=20, padx=20)

    def update_guide(self, languages, current_language):
        self.languages = languages
        self.current_language = current_language
        if self.guide_window and self.guide_window.winfo_exists():
            self.guide_label.config(text=self.languages[self.current_language]["guide_text"])

    def toggle(self):
        if self.guide_window is None or not self.guide_window.winfo_exists():
            self.create_window()
        if self.guide_window.winfo_viewable():
            self.guide_window.withdraw()
        else:
            self.guide_window.deiconify()
