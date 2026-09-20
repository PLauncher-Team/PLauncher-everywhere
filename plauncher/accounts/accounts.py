import hashlib
import uuid

class AccountsManager:
    def __init__(self, master):
        self.master = master
        pass
    
    @staticmethod
    def get_offline_uuid(username):
        data = f"OfflinePlayer:{username}".encode("utf-8")
        return str(uuid.UUID(bytes=hashlib.md5(data).digest(), version=3))
    
    def get_usernames(self):
        values = []
        for account in self.master.settings_manager.settings.accounts.accounts_list:
            values.append(f"{account['name']} ({account['type']})")
        return values