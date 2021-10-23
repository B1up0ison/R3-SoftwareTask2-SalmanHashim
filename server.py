
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostname()
port = 1337

s.bind((host,port))
s.listen(0)

con,addr=s.accept()
print("connected with", addr)

while True:
    #messag=input("send message to client: ")
    #con.send(messag.encode())
    #print("waiting for response")
    c_message=con.recv(1024)
    print("",c_message.decode())