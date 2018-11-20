import socket
host=socket.gethostname()
port=9999
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind((host,port))
print("Listening")
soc.listen(5)
while True:
    con,addr=soc.accept()
    s=con.recv(4098)
    if not s:
        break
    s=s.decode()
    print("Computing............")
    r=eval(s)
    print(type(r))
    r=str(r)
    con.sendall(r.encode())
print("Disconnected")