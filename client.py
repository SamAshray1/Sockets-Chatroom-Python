import socket
import threading

def readMessages(s):
    while True:
        try:
            recvMessage = s.recv(1024).decode()

            if recvMessage:
                print(recvMessage)
        except:
            s.close()
            break

def sendMessages(s):
    while True:
        try:
            messageToSend = input()

            if messageToSend != 'close':
                s.send(messageToSend.encode())

            elif messageToSend == 'close':
                s.close()
                break
        except:
            s.close()
            break

if __name__ == "__main__":
    s = socket.socket()
    port = 12345

    s.connect(('127.0.0.1', port))

    t1 = threading.Thread(target=readMessages, args=(s, ))
    t2 = threading.Thread(target=sendMessages, args=(s, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    s.close()

