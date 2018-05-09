import sys
from coursera_python.module3.SimpleSocketServer import start_socket_server

port = int(sys.argv[1])

print(f'Starting server on port {port}')

start_socket_server(port)
