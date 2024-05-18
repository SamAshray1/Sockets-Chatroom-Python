import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfully.")
except socket.error as err:
    print("Socket creation failed due to ", err)

port = 80

try:
    host_ip = socket.gethostbyname('www.samuelblog.in')
    print("Host ip is ", host_ip)
except socket.gaierror as err:
    print("Error", err)
    sys.exit()

try:
    s.connect((host_ip, port))
    print("Connected successfully")
except socket.error as err:
    print(err)

