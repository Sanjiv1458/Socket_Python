import socket

# Create a socket object
s = socket.socket()

# Define the port on which we want to connect
port = 55000

# connect to the server on local computer
s.connect(('127.0.0.1', port))
print(s.recv(1024).decode())
message = input(" -> ")  # take input

# loop will intrrupt until client client say "bye" to server
while message.lower().strip() != 'bye':
    s.send(message.encode())  # send message
    data = s.recv(1024).decode()  # receive response
    print('Server message: ' + data)  # show in terminal
    message = input(" -> ")  # again take input
s.close()  # close the connection