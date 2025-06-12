import customtkinter as ctk
import tkinter.font as tkfont


def build_settings_frame(master):
    frame = ctk.CTkFrame(master)
    label_font = ("Helvetica", 14)

    # ========== Left column ==========
    left_col = ctk.CTkFrame(frame)
    left_col.pack(side="left", expand=True, fill="both", padx=10)

    # ========== Right column (Font Picker) ==========
    right_col = ctk.CTkFrame(frame)
    right_col.pack(side="left", expand=True, fill="both", padx=10)

    # ctk.CTkLabel(right_col, text="Choose Font:", font=label_font).pack(
    #     anchor="w", pady=(5, 0)
    # )

    # search_var = ctk.StringVar()
    # search_entry = ctk.CTkEntry(
    #     right_col, textvariable=search_var, placeholder_text="Search fonts..."
    # )
    # search_entry.pack(fill="x", pady=5)

    # font_list_frame = ctk.CTkScrollableFrame(right_col, height=160)
    # font_list_frame.pack(fill="both", expand=True, pady=5)

    # all_fonts = sorted(tkfont.families())
    # font_labels = []

    # def filter_fonts(*_):
    #     typed = search_var.get().lower()
    #     for label in font_labels:
    #         label.pack_forget()
    #     for label in font_labels:
    #         if typed in label.cget("text").lower():
    #             label.pack(fill="x", padx=5, pady=1)

    # def on_font_click(font_name):
    #     print("Selected font:", font_name)
    #     # TODO: Save selected font to settings or apply it

    # for fname in all_fonts:
    #     lbl = ctk.CTkLabel(font_list_frame, text=fname, anchor="w", cursor="hand2")
    #     lbl.bind("<Button-1>", lambda e, f=fname: on_font_click(f))
    #     font_labels.append(lbl)

    # filter_fonts()
    # search_var.trace_add("write", filter_fonts)

    return frame
