import socket
import threading
from _thread import *
import pickle
#pickle use to send objects by serializing them
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server=socket.gethostbyname(socket.gethostname())
s.bind((server,5555))
s.listen(2)
print("waiting for connection to be connected")


def handle_client(conn,addr):
    print("client at ",addr,"connected to the server")
    run=True
    while run:
        msg = conn.recv(1024).decode("utf-8")
        if msg:
            print(f"Message from {addr} is ", msg)
        elif not msg:
            run=False
    conn.close()





while True:

    conn,addr=s.accept()
    thread=threading.Thread(target=handle_client, args=(conn,addr,))
    thread.start()
    print(f" [Active Connections : ]  {threading.active_count()-1}")
    #message="hello client you are connected"
    #print("message from client to server is ",conn.recv(1024).decode("utf-8"))
    #conn.send(bytes(message,"utf-8"))


