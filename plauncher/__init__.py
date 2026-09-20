import customtkinter as ctk
from .themes import ThemeManager
from .pages import VerticalPagePanel
from .fonts import load_fonts
from .storage import StorageManager
from .versions import VersionsManager
from .ctk_fixes import patch_progressbar_zero

patch_progressbar_zero()
load_fonts()


class PLauncher(ctk.CTk):
    def __init__(self,
                 **kwargs):
        super().__init__(**kwargs)

        self.ThemeManager = ThemeManager(self)
        self.ThemeManager.set_random_theme()
        
        self.StorageManager = StorageManager()
        self.VersionsManager = VersionsManager(self)

        self.geometry("800x500")
        self.resizable(0, 0)
        self.title("PLauncher")

        self.menu_frame = VerticalPagePanel(self, border_width=0)
        self.menu_frame.nav_frame.configure(border_width=0)
        self.menu_frame.pack(side="left", fill="both", expand=True)