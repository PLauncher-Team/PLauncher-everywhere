import psutil

class JavaManager:
    def __init__(self):
        self.memory_max_mb = ((psutil.virtual_memory().total + 1024**3 - 1) // 1024**3) * 1024