import socket
import threading
from logo import Logo
import time
from datetime import datetime
import colors
import os
os.system('color')


class ServerSocket:
    def __init__(self):
        self.PORT = 12345
        self.SIZE = 1024
        self.HOST = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logo = Logo()


    def start(self):
        self.logo.draw()

        self.socket.bind((self.HOST, self.PORT))
        print(f"Server binded to port: {self.PORT}")
        self.socket.listen(5)
        print(f"Server listening to port: {self.PORT}")

        while True:
            client, address = self.socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(client, address))
            thread.start()
            print(f"Active connections: {threading.active_count() - 1 }")


    def handle_client(self, client, address):
        time = datetime.now().replace(microsecond=0)

        print(colors.green(f"{time} | New connection from: {address[0]}"))
        while True:
            try:
                data = client.recv(self.SIZE)
                print(address[0], data.decode("utf-8"))
            except:
                print(colors.red(f"{time} | Lost connection to {address[0]}"))
                return


if __name__ == "__main__":
    server = ServerSocket()
    server.start()