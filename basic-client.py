import socket

s = socket.socket()
port = 12345

# s.bind(('', port))

s.connect(('127.0.0.1', port))

# print(s.recv(1024).decode())
s.send("Hi I've connected\n Sam".encode())

while True:
    sendMessage = input()
    if sendMessage == "exit":
        break
    else:
        s.send(sendMessage.encode())
s.close