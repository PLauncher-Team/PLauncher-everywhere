import minecraft_launcher_lib as mll
from concurrent.futures import ThreadPoolExecutor
import customtkinter as ctk

class VersionsManager:
    def __init__(self, master: ctk.CTk):
        self.versions = {}
        self.master = master
        
        loaders = list(mll.mod_loader.list_mod_loader())

        self._executor = ThreadPoolExecutor(max_workers=len(loaders))
        for loader in loaders:
            self._executor.submit(self._load_versions, loader)
        
        self.master.bind("<Map>", self._display_version)
    
    def _display_version(self, event=None):
        # Versions page load
        self.master.VerticalPagePanel.pages[2]

    def _load_versions(self, loader: str):
        mod_loader = mll.mod_loader.get_mod_loader(loader)
        self.versions[loader] = mod_loader.get_minecraft_versions(False)