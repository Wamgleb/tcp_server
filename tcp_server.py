import socket 
import threading

SOCKET_IP = "127.0.0.1"
SOCKET_PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SOCKET_IP, SOCKET_PORT))
server.listen(10)

print("[+] Server listenning on {0}:{1}".format(SOCKET_IP, SOCKET_PORT))
client, addr = server.accept()
client.send("I am the server accepting connections...".encode())
print("[+] Accepted connection from {0}:{1}".format(addr[0], addr[1]))

def handle_client(socket_client):
    request = socket_client.recv(1024)
    print("[*] Received request : {0} from client {1}".format(request, socket_client.getpeername()))
    socket_client.send(bytes("ACK","utf-8"))
while True:
    handle_client(client)
client_socket.close()
server.close()