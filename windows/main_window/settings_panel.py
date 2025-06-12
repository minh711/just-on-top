import customtkinter as ctk
import tkinter.font as tkfont


def build_settings_frame(master):
    frame = ctk.CTkFrame(master)
    label_font = ("Helvetica", 14)

    # ========== Left column ==========
    left_col = ctk.CTkFrame(frame)
    left_col.pack(side="left", expand=True, fill="both", padx=10)

    # ========== Right column ==========
    right_col = ctk.CTkFrame(frame)
    right_col.pack(side="left", expand=True, fill="both", padx=10)

    return frame
