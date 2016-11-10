import sys
from socket import *
from Queue import Queue
from threading import Thread
import os
import signal


def _workers(swimmer):

	while True:

		work_socket=swimmer.get()
		work_address=swimmer.get()
		active=True
		while active==True:
			receive=work_socket.recv(2048)
			if not receive: break
			if receive[:12]=="KILL_SERVICE":
				print "Killing!!"
				work_socket.close()
				active=False
			elif receive[:4]=="HELO":
				print "HELO Received: "+receive
				#msg=receive + "\nIP: " + work_address + "\nPort: " + str(work_socket) + "\nStudentID:13319829\n"
				msg="%sIP:%s\nPort:%s\nStudentID:13319829\n"%(receive,str(work_address),work_socket)
				work_socket.sendall(msg)
				print "HELO Sent"	
			else:
				print "other Received:"+receive
				message=receive[:-2].upper()
				work_socket.sendall(message)
		if active==False:
			os.kill(os.getpid(),signal.SIGINT)					
	
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
		try:
			client_socket,address=sock.accept()
			pool.put(client_socket)
			pool.put(address)
		except KeyboardInterrupt:
			print "\nSTOPPED"
			break


if __name__ == '__main__':
	_server(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
