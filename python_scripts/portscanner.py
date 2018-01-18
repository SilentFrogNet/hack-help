import socket

target = input("Enter the IP address to scan: ")
portrange = input("Enter the port range to scan (es 5-200): ")

lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])

print("Scanning host {} from port {} to port {}".format(target, lowport, highport))

for port in range(lowport, highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if status == 0:
        print("Port {} is OPEN".format(port))
    s.close()
