import customtkinter as ctk
from .themes import ThemeManager
from .pages import VerticalPagePanel

for font in [
    "Inter_18pt-Regular.ttf",
    "Inter_18pt-Medium.ttf",
    "Inter_18pt-SemiBold.ttf",
    "Inter_18pt-Bold.ttf",
    "JetBrainsMono-Regular.ttf",
    "JetBrainsMono-SemiBold.ttf",
]:
    ctk.FontManager.load_font(f"plauncher/fonts/{font}")

class PLauncher(ctk.CTk):
    def __init__(self,
                 **kwargs):
        super().__init__(**kwargs)

        self.ThemeManager = ThemeManager(self)
        self.ThemeManager.set_random_theme()

        self.geometry("800x500")
        self.resizable(0, 0)
        self.title("PLauncher")

        self.menu_frame = VerticalPagePanel(self, border_width=0)
        self.menu_frame.nav_frame.configure(border_width=0)
        self.menu_frame.pack(side="left", fill="both", expand=True)