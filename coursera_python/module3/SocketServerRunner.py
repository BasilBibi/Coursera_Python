import sys
import socket
from coursera_python.module3.SimpleSocketServer import start_socket_server

port = int(sys.argv[1])

print(f'Starting server on port {port}')

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start_socket_server(sock, port)
finally:
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
