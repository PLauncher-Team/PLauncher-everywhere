import customtkinter as ctk
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = CURRENT_DIR

def load_fonts():
    for font in [
        "Inter_18pt-Regular.ttf",
        "Inter_18pt-Medium.ttf",
        "Inter_18pt-SemiBold.ttf",
        "Inter_18pt-Bold.ttf",
        "JetBrainsMono-Regular.ttf",
        "JetBrainsMono-SemiBold.ttf",
    ]:
        ctk.FontManager.load_font(f"{FONTS_DIR}/{font}")
