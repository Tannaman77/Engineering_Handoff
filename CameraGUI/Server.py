import numpy as np
import socket, sys, cv2, PyQt5



server_status = 'open'
HOST = socket.gethostname()
HOST = socket.gethostbyname(HOST)
print(HOST)
PORT = 1234



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)



while server_status == 'open':
	clientsocket, address = s.accept()
	print(f" connection from {clientsocket},  done.")	

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
