import socket
import traceback


def start_socket_server(server_socket, port):
    try:
        addr = ('', port)
        server_socket.bind(addr)

        server_socket.listen(5)

        client_socket, client_address = server_socket.accept()

        print(f'{client_socket}:{client_address} has connected.')

        while True:
            data = client_socket.recv(512)
            print(data.decode())

    except Exception:
        traceback.print_exc()

    finally:
        server_socket.shutdown(socket.SHUT_RDWR)
        server_socket.close()


def start_socket_client(sock, host, port):
    try:
        sock.connect((host, port))

        print(f'You are connected to {sock}')

        while True:
            msg = input()
            if msg == 'QUIT': break
            msg = msg.encode()
            sock.send(msg)

    except Exception:
        traceback.print_exc()

    finally:
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
