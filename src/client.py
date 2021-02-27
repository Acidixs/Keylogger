import socket
import os 
from dotenv import load_dotenv

class ClientSocket:
    def __init__(self):
        self.PORT = 12345
        load_dotenv()

    def send_message(self, msg):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        msg = str.encode(msg, "utf-8")
        mysocket.connect((os.getenv("SERVER_IP"), self.PORT))
        mysocket.send(msg)
        mysocket.close()
