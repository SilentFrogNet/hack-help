import socket

common_services = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    80: 'HTTP',
    109: 'POP2',
    110: 'POP3',
    137: 'NetBIOS',
    138: 'NetBIOS',
    139: 'NetBIOS',
    443: 'HTTPS'
}

target = input("Enter the IP address to scan: ")
portrange = input("Enter the port range to scan (es 5-200): ")

lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])

print("Scanning host {} from port {} to port {}".format(target, lowport, highport))

for port in range(lowport, highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if status == 0:
        common_text = ""
        if int(port) in common_services.keys():
            common_text = " - Default protocol: {}".format(common_services[int(port)])
        print("Port {} is OPEN{}".format(port, common_text))
    s.close()
