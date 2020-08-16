import socket
import time


c = socket.socket()
server=socket.gethostbyname(socket.gethostname())
c.connect((server, 5555))
time.sleep(4)

message = "hello server i am at 40 x and 30 y"
c.send(bytes(message, "utf-8"))

# print("message from server is : ",c.recv(1024).decode())




