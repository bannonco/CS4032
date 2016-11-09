import sys
import socket
import Queue
from threading import Thread



def worker
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_address=('localhost',8000)


client_socket.connect(socket_address)

receive=client_socket.recv(1024)
client_socket.close()

if data=="KILL_SERVICE\n"

else if data=="HELO text\n"
"HELO text\nIP:[ip address]\nPort:[port number]\nStudentID:13319829\n"

else

if __name__ == '__main__':
