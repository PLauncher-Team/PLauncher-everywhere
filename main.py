import sys
from pathlib import Path
from filelock import FileLock, Timeout

def main():
    lock_path = Path.home() / ".plauncher.lock"
    
    lock = FileLock(lock_path, timeout=0)

    try:
        with lock:
            from plauncher import PLauncher

            root = PLauncher()
            root.mainloop()

    except Timeout:
        sys.exit(1)

if __name__ == "__main__":
    main()