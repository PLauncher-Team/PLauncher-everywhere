import os
import random
import customtkinter as ctk
import json

class ThemeManager:
    def __init__(self, master: ctk.CTk):
        self.current_theme: str = ""
        self.themes_path: str = "plauncher/themes/"
        self.avaible_themes: list = self.get_themes()
        self.master = master
        
    def get_themes(self):
        return [f"{self.themes_path}{theme}" for theme in os.listdir(self.themes_path) if theme.endswith(".json")]
    
    def set_random_theme(self):
        random_theme = random.choice(self.avaible_themes)
        self.set_theme(random_theme)
    
    def set_theme(self, theme_path):
        ctk.set_default_color_theme(theme_path)
        self.master.configure(fg_color=ctk.ThemeManager.theme["CTk"]["fg_color"])