import socket


class ClientSocket:
    def __init__(self):
        self.PORT = 12345

    def send_message(self, msg):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        msg = str.encode(msg, "utf-8")
        mysocket.connect(("127.0.0.1", self.PORT))
        mysocket.send(msg)
        mysocket.close()
