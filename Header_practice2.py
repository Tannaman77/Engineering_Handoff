import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
HOST = socket.gethostbyname(HOST)
PORT = 1224
s.bind((HOST, PORT))

msg = "Welcome to the Server!"
print(f'{len(msg):<10}'+ msg)
f = len(msg)
print(f)
