import tkinter as tk

class GuideWindow:
    def __init__(self, root, languages, current_language):
        self.root = root
        self.languages = languages
        self.current_language = current_language
        self.guide_window = None
        self.text_widget = None
        self.create_window()

    def create_window(self):
        self.guide_window = tk.Toplevel(self.root)
        self.guide_window.title("Guide")
        self.guide_window.geometry("360x400")
        self.guide_window.configure(bg='#F0F0F0')
        self.guide_window.withdraw()

        self.text_widget = tk.Text(
            self.guide_window,
            wrap='word',
            bg='#F0F0F0',
            fg='black',
            font=('Helvetica', 12),
            borderwidth=0
        )
        self.text_widget.pack(fill='both', expand=True, padx=20, pady=20)
        self.text_widget.insert('1.0', self.languages[self.current_language]["guide_text"])
        self.text_widget.config(state='disabled')  # Make it read-only

    def update_guide(self, languages, current_language):
        self.languages = languages
        self.current_language = current_language
        if self.text_widget:
            self.text_widget.config(state='normal')
            self.text_widget.delete('1.0', 'end')
            self.text_widget.insert('1.0', self.languages[self.current_language]["guide_text"])
            self.text_widget.config(state='disabled')

    def toggle(self):
        if self.guide_window is None or not self.guide_window.winfo_exists():
            self.create_window()
        if self.guide_window.winfo_viewable():
            self.guide_window.withdraw()
        else:
            self.guide_window.deiconify()
