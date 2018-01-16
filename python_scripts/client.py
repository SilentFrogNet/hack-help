import socket

SRV_ADDR = input("Type the server IP address: ")
SRV_PORT = int(input("Type the server port: "))

print("Listening on {}:{}".format(SRV_ADDR, SRV_PORT))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SRV_ADDR, SRV_PORT))
print("Connection enstablished...")

message = input("Message to send: ")
s.sendall(message.encode())
s.close()
