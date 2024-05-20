import socket

s = socket.socket()
port = 12345

s.connect(('127.0.0.1', port))

print(s.recv(1024).decode())
username = input()
s.send(username.encode())
print(s.recv(1024).decode())

while True:

    try:
        recvMessage = s.recv(1024).decode()
        if recvMessage:
            print(recvMessage)
        else:
            break
    except:
        continue

    try:
        sendMessage = input()
        if sendMessage == "exit":
            break
        else:
            s.send(sendMessage.encode())
    except:
        continue

    
s.close