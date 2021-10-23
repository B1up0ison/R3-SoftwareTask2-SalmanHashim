import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostname()
port = 1337

s.bind((host,port))
s.listen(0)

con,client=s.accept()
print("connected with", client)

while True:
    c_message=con.recv(1024)
    print("",c_message.decode())