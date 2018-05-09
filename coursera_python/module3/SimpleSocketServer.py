import socket
import traceback


def start_socket_server(port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = ('', port)
        sock.bind(addr)

        sock.listen(5)

        client, client_address = sock.accept()

        print(f'{client}:{client_address} has connected.')

        while True:
            data = client.recv(512)
            print(data.decode())

    except Exception:
        traceback.print_exc()

    finally:
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()


def start_socket_client(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
