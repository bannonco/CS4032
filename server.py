import sys
from socket import *
from Queue import Queue
from threading import Thread



def _workers(swimmer):

	while True:

		work_socket=swimmer.get()
		work_address=swimmer.get()
		active=True
		while active:
			receive=client_socket.recv(1024)
			if receive=="KILL_SERVICE\n":
				socket.close()
				active=False
			elif receive[:4]=="HELO":
				msg=data+"IP:"+work_address+"\nPort:"+work_socket+"\nStudentID:13319829\n"
				work_socket.sendall(msg)	
			else:
				message=receive[:-2].upper()
				work_socket.sendall(message)				
			
	work_socket.close()

def _server(hostname,port_number,numb_of_workers):
	sock=socket(AF_INET,SOCK_STREAM)
	sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	sock.bind((hostname,port_number))
	sock.listen(10)	
	pool=Queue(numb_of_workers)

	for i in range(numb_of_workers):
		thread= Thread(target=_workers,args=(pool,))
		thread.daemon=True
		thread.start()
	while True:
		client_socket,address=sock.accept()
		pool.put(client_socket)
		pool.put(address)

if __name__ == '__main__':
	_server(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
