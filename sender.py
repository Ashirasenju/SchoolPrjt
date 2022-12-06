import socket

hote = "localhost"
port = 5566

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))

socket.send("Hey my name is Olivier!".encode())

