import socket
import threading

clients = []

def broadcastMessage(c, message, username):
    for client in clients:
        if client != c:
            client.send((f"{username}: {message}").encode())
        else:
            continue

def handleClient(c, addr):
    c.send('Thank you for connecting\nPlease enter your name:'.encode())
    username = c.recv(1024).decode()

    c.send(f"Thanks for joining {username}, continue chatting!".encode())

    while True:
        try:
            message = c.recv(1024).decode()
            if message:
                print(f"{username}: {message}")
                broadcastMessage(c, message, username)
            else:
                c.close()
                clients.remove(c)
                break          

        except:
            c.close()
            clients.remove(c)
            break


def createThread(s):
    c, addr = s.accept()
    clients.append(c)
    # print(clients)
    t1 = threading.Thread(target=handleClient, args=(c, addr))
    t1.start()

def closeConnections(s):
    while True:
        try:
            serverInput = input()

            if serverInput == 'exit':
                s.close()
                break
        except:
            continue


if __name__ == "__main__":
    s = socket.socket()
    port = 12345

    s.bind(('', port))
    s.listen(5)
    print("Server listening!")

    closeCheckThread = threading.Thread(target=closeConnections, args=(s, ))
    closeCheckThread.start()
    
    while True:
        createThread(s)

    s.close()