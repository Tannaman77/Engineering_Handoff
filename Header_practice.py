import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = input('Whats the host name? ")
PORT = 1224
s.connect((HOST, PORT))
