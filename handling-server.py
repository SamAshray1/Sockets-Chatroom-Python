# first of all import the socket library 
import socket	

def handleClient():
    while True: 
        # Establish connection with client. 
        c, addr = s.accept()	 
        print ('Got connection from', addr )

        c.send('Thank you for connecting\nPlease enter your name:'.encode())
        username = c.recv(1024).decode()

        c.send(f"Thanks for joining {username}, continue chatting!".encode())

        while True:
            msgRecv = c.recv(1024).decode()
            if msgRecv == "hi":
                print("matched")

            if msgRecv == "close":
                c.close()
                break
            else:
                print(f"{username}: ",msgRecv)

        # Breaking once connection closed
        break
    
    # Close the connection with the client 
    c.close()
    
    return 0

if __name__ == "__main__":    
    # next create a socket object 
    s = socket.socket()		 
    print ("Socket successfully created")

    # reserve a port on your computer in our 
    port = 12345			

    # Next bind to the port 

    s.bind(('', port))		 
    print ("socket binded to %s" %(port)) 

    # put the socket into listening mode 
    s.listen(5)	 
    print ("socket is listening")		 

    handleClient()






