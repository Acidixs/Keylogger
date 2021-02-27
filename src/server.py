import socket


PORT = 12345
SIZE = 1024
HOST = ""

print("yo")

s = socket.socket()
s.bind((HOST, PORT))
print(f"Server binded to {PORT}")

s.listen(5)
print(f"Server listening to {PORT}")

while True:
    client, address = s.accept()
    print("Received connection from", address)
    data = client.recv(SIZE)
    print("Client:", data.decode("utf-8"))
    client.close()