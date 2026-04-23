import socket

HOST = '127.0.0.1'
PORT = 57777
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
reponse = socket.recv(1024).decode()
print(reponse)
