import socket
import time
import subprocess

class ClientSocket:
    def __init__(self):
        self.PORT = 12345
        self.IP = "127.0.0.1"

    def send_message(self, msg):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.IP, self.PORT))
        msg = str.encode(msg, "utf-8")
        self.socket.send(msg)
        self.socket.close()


