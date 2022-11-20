import sys
import socket

args = sys.argv
hostname = args[1]
port = int(args[2])
password = args[3]

client_socket = socket.socket()
address = (hostname, port)
client_socket.connect(address)
data = password.encode()
client_socket.send(data)
response = client_socket.recv(1024)
response = response.decode()
client_socket.close()
print(response)
