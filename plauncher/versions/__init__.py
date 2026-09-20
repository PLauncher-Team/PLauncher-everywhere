import minecraft_launcher_lib as mll
from concurrent.futures import ThreadPoolExecutor
import customtkinter as ctk


class VersionsManager:
    def __init__(self, master: ctk.CTk):
        self.versions_by_loader = {}
        self.master = master
        
        all_loaders = set(mll.mod_loader.list_mod_loader())
        self.pending_loaders = all_loaders.copy()
        self.executor = ThreadPoolExecutor(max_workers=len(all_loaders))
        for loader in all_loaders:
            self.executor.submit(self._load_versions_for_loader, loader)

        self.master.after(0, self._update_display)

    def _update_display(self):
        if self.master.winfo_viewable() and self.versions_by_loader:
            versions_page = self.master.menu_frame.pages[3]
            ready_loaders = self.versions_by_loader.keys() & self.pending_loaders
            self.pending_loaders -= ready_loaders
            for loader in ready_loaders:
                versions_page.loader_versions[loader] = self.versions_by_loader[loader]
            
            if ready_loaders:
                versions_page.update_loaders_list(self.versions_by_loader)

        if not self.pending_loaders:
            return

        self.master.after(100, self._update_display)

    def _load_versions_for_loader(self, loader: str):
        mod_loader = mll.mod_loader.get_mod_loader(loader)
        self.versions_by_loader[loader] = mod_loader.get_minecraft_versions(False)