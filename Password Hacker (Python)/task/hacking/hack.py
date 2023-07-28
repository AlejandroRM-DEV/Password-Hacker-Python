import itertools
import socket
import sys
from string import ascii_lowercase, digits

ip_address = sys.argv[1]
port = int(sys.argv[2])

chars = list(''.join((ascii_lowercase, digits)))

with socket.socket() as client_socket:
    address = (ip_address, port)
    client_socket.connect(address)

    for i in range(1, 4):
        combinations = itertools.product(chars, repeat=i)
        for combination in combinations:
            password = "".join(combination)
            client_socket.send(password.encode('utf8'))
            response = client_socket.recv(1024)
            if response.decode('utf8') == 'Connection success!':
                print(password)
