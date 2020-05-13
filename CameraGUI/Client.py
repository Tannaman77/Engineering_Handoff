import  numpy as np
import socket, sys, cv2, PyQt5

PORT = 1234
HOST = input('Enter the IP: ')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
