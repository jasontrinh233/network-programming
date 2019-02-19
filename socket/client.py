# Quang Trinh
# Socket Programming
# Client Program


import socket
import sys

# create socket object 
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket successfully created")
except socket.error as err:
	print("Failed to create socket. Error " + str(err))
	sys.exit()

# get server_address
local_hostname = socket.gethostname()
ip = socket.gethostbyname(local_hostname)
port = 6868
server_address = (ip, port)

# connect socket to server
try:
	s.connect(server_address)
	print("connecting to server %s @ %s on port %s" % (local_hostname, ip, port))
except socket.error as err:
	print("Unable to connect to server. Error " + str(err))
	sys.exit()

# send data to server
try:
	cmd = str(input("Type your message: "))
	s.sendall(str.encode(cmd))
	print("Message sent")
except socket.error as err:
	print("Unable to send message. Error" + str(err))
	sys.exit()

# recieving response from server
data = s.recv(256).decode()

# display response from server
print("Response from server: " + data)

# close connection
s.close()
print("Connection closed")
