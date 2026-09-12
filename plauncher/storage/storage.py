from minecraft_launcher_lib.utils import get_minecraft_directory
from minecraft_launcher_lib.vanilla_launcher import ensure_vanilla_launcher_profiles_exists
import os

class StorageManager:
    def __init__(self):
        self.minecraft_dir = get_minecraft_directory()
        os.makedirs(self.minecraft_dir, exist_ok=True)
        
        self._create_environment()
    
    def _create_environment(self) -> dict:
        folders = [
            "assets",
            "libraries",
            "versions",
            "saves",
            "resourcepacks",
            "shaderpacks",
            "mods",
            "screenshots",
            "logs",
        ]
    
        for folder in folders:
            os.makedirs(os.path.join(self.minecraft_dir, folder), exist_ok=True)
        
        ensure_vanilla_launcher_profiles_exists(self.minecraft_dir)