#client

import socket
import sys

HOST=socket.gethostname()
PORT=9999

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect((HOST,PORT))

print ("[+]Connecteed to the server")

file_name= input("Enter the file to send:")

try:
    file=open(file_name,"rb")
    data=file.read()
    print ("Sending file....")
    soc.sendall(data)
    file.close()
    soc.close()
    print ("[-]Disconnecteed")

except FileNotFoundError:
    print ("ERROR:File not found")


