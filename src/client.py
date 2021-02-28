import socket
import time
import subprocess

class ClientSocket:
    def __init__(self):
        self.PORT = 12345
        self.IP = "127.0.0.1"

    def send_message(self, msg):
        msg = str.encode(msg, "utf-8")
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect((self.IP, self.PORT))
        mysocket.send(msg)
        mysocket.close()

    def send_ip(self):
        s = subprocess.Popen("ipconfig",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = s.stdout.read() + s.stderr.read()

        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect((self.IP, self.PORT))
        mysocket.send(result)
        mysocket.close()
