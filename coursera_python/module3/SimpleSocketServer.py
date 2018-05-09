import socket
import traceback


def start_socket_server(sock, port):

    try:
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
