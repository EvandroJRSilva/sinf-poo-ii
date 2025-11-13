import socket

HOST = "127.0.0.1"  # O IP ou o nome do servidor
PORT = 65432        # A porta usada pelo servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        data = s.recv(1024)

print(f"Received {data.decode('utf-8')}")