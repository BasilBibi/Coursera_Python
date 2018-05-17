def start_socket_server(server_socket, port):
    addr = ('', port)
    server_socket.bind(addr)
    server_socket.listen(5)

    client_socket, client_address = server_socket.accept()

    print(f'{client_socket}:{client_address} has connected.')

    while True:
        data = client_socket.recv(512)
        print(data.decode())


def start_socket_client(client_socket, host, port):
    client_socket.connect((host, port))

    print(f'You are connected to {client_socket}')

    while True:
        msg = input()
        if msg == 'QUIT': break
        msg = msg.encode()
        client_socket.send(msg)
