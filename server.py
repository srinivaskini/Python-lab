#server

import socket
import sys

HOST= socket.gethostname()
PORT= 9999

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind((HOST,PORT))
soc.listen(1)
print ("Listening.........")

while True:
    conn,addr=soc.accept()
    print ("[+]Client connected:",addr)
    file=open("recv.txt","wb")
    while True:
        data=conn.recv(4096)
        if not data:
            break
        file.write(data)
    file.close()
    print ("[+]Download complete")
    conn.close()
    print ("[-]Client disconnected")

