import sys
import socket
from coursera_python.module3.SimpleSocketServer import start_socket_client

host = sys.argv[1]
port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

start_socket_client(sock, host, port)
