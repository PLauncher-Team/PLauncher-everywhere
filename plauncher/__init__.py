import customtkinter as ctk
from .themes import ThemeManager
from .pages import VerticalPagePanel
from .fonts import load_fonts
from .appstorage import StorageManager, SettingsManager
from .versions import VersionsManager
from .ctk_fixes import patch_progressbar_zero
from .java import JavaManager
from .accounts import AccountsManager

patch_progressbar_zero()
load_fonts()


class PLauncher(ctk.CTk):
    def __init__(self,
                 **kwargs):
        super().__init__(**kwargs)
 
        self.theme_manager = ThemeManager(self)
        self.theme_manager.set_random_theme()
        
        self.storage_manager = StorageManager()
        self.settings_manager = SettingsManager()
        self.versions_manager = VersionsManager(self)
        self.accounts_manager = AccountsManager(self)
        self.java_manager = JavaManager()

        self.geometry("800x500")
        self.resizable(0, 0)
        self.title("PLauncher")

        self.menu_frame = VerticalPagePanel(self, border_width=0)
        self.menu_frame.nav_frame.configure(border_width=0)
        self.menu_frame.pack(side="left", fill="both", expand=True)