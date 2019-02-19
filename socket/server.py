# Quang Trinh
# Socket Programming
# Server Program


import socket
import sys

# create socket object
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket successfully created")
except socket.error as err:
	print("Failed to create socket. Error: " + str(err))
	sys.exit()

# get server_address
local_hostname = socket.gethostname()
ip = socket.gethostbyname(local_hostname)
port = 6868
server_address = (ip, port)

# bind socket
try:
	s.bind(server_address)
	print("starting up on %s port %s" % (server_address))
except socket.error as err:
	print("Failed to bind socket. Error " + str(err))
	sys.exit()

# listen for incomming connection
try:
	s.listen(1) # 1 connection at a time
	print("waiting for connection...")
except socket.error as err:
	print("Unable to put in listenning mode. Error " + str(err))

# accept client connection
try:
	connection, client_address = s.accept()
	print("Accepting connection from %s port %s" % (client_address))
except socket.error as err:
	print("Unable to accept connection. Error " + str(err))

# receive data and print decoded data to console
while True:
	data = connection.recv(256).decode() # 256 bytes buffer size
	if data:
		msg = ""
		for i in range(0, len(data)):
			msg += chr(ord(data[i]) + 1)

		# message from client
		print("Message from client: " + data)
		connection.sendall(msg.encode())
	else:
		break

# respose message to send to client
print("Response message: %s" % str(msg))

# connection close
s.close()
print("Connection closed")