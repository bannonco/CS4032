from socket import *
import thread
import sys
import time


def sockets(hostname,port_number,msg):

	sock=socket(AF_INET, SOCK_STREAM)
	sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	sock.connect((hostname,port_number))

	while True:
		sock.send(msg)
		ret_msg=sock.recv(2048)
		print "Received message:"+ret_msg

	sock.close()

for x in range(2):
	pool=thread.start_new(sockets,(sys.argv[1],int(sys.argv[2]),sys.argv[3]))

time.sleep(10)
