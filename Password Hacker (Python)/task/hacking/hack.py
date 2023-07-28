import socket
import sys

ip_address = sys.argv[1]
port = int(sys.argv[2])
message = sys.argv[3]

with socket.socket() as client_socket:
    address = (ip_address, port)
    client_socket.connect(address)
    client_socket.send(message.encode())
    response = client_socket.recv(1024)
    print(response.decode())
