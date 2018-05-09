import sys
from coursera_python.module3.SimpleSocketServer import start_socket_client

host = sys.argv[1]
port = int(sys.argv[2])

start_socket_client(host, port)
