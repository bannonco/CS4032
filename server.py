import sys
import socket
import Queue
from threading import Thread



def workers(swimmer)

	while True:

		socket=swimmer.get();
		address
		active=True
		while active
			receive=client_socket.recv(1024)


			if data=="KILL_SERVICE\n"
				socket.kill()
				active=False

			elif data[:4]=="HELO":
				msg=data+"IP:"[ip address]"\nPort:"[port number]"\nStudentID:13319829\n"
	
			else

			
	socket.close()

def server(hostname,port_number,numb_of_workers)
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock=socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	sock.bind((hostname,port_number))
	sock.listen(5)	
	pool=Queue(numb_of_workers)
	
	for i in range(numb_of_workers)
		thread= Thread(target=worker,args=(pool,))
		thread.daemon=True
		thread.start()

if __name__ == '__main__':
	server(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
