import socket

class ClientSocket:
    def __init__(self):
        self.PORT = 12345
        self.IP = "127.0.0.1"
        self.cs = self.start()

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.IP, self.PORT))
        return s


    def send_message(self, msg):
        msg = str.encode(msg, "utf-8")
        self.cs.send(msg)
