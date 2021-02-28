import socket
from logo import Logo

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


    def get_info(self):
        while True:
            client, address = self.socket.accept()
            print("Received connection from", address)
            data = client.recv(self.SIZE)
            print("Client:", data.decode("utf-8"))
            client.close()


if __name__ == "__main__":
    server = ServerSocket()
    server.start()
    server.get_info()