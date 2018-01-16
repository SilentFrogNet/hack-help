import http.client

print("** This program checks if a specific resource is available on the webserver **\n")

host = input("Insert the host/IP: ")
port = input("Insert the port(default:80): ")
url = input("Insert the url: ")

if port == "":
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('GET', url)
    response = connection.getresponse()
    if response.status == 200:
        print("Resource FOUND on the server ({})".format(response.status))
    elif response.status == 404:
        print("Resource NOT FOUND on the server ({})".format(response.status))
    elif response.status == 403:
        print("Access to the resource FORBIDDEN ({})".format(response.status))
    connection.close()
except ConnectionRefusedError:
    print("Connection failed")
