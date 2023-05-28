import socket

# Create a socket object
s = socket.socket()
print("Socket successfully created")

# Define the port on which we want to connect
port = 55000

s.bind(('', port))
print("socket binded to %s" % (port))

s.listen(5)
print("socket is listening")

# Establish connection with client.
c, addr = s.accept()
print('Got connection from: ', addr)
c.send('Thank you for connecting: server'.encode())

# a forever loop until we interrupt it or an error occurs
while True:
    data = c.recv(1024).decode()
    if not data:
        # if data is not received break
        break
    print("Server: " + str(data))
    message = input(' -> ')
    c.send(message.encode())
c.close()
