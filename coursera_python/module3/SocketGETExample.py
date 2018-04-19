import socket


def strip_cr_lf(s): return s.replace("\n", "").replace("\r", "")


def get_url(host, port, url):

    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect( (host, port) )
        full_url = "GET " + url + " HTTP/1.0\r\n\r\n"
        cmd = full_url.encode()
        sock.send(cmd)

        data_str = ""
        while True:
            data = sock.recv(512)
            print(data)
            if len(data) < 1: break
            decoded = [l for l in data.decode().split("\r\n") if( ":" not in l and "HTTP" not in l)]
            data_str = data_str + "".join(decoded)
        return strip_cr_lf(data_str)
    finally:
        sock.close()


class UrlUtils:

    def __init__(self, sock):
        self.sock = sock

    def strip_cr_lf(self,s):
        return s.replace("\n", "").replace("\r", "")

    def get_url(self, host, port, url):
        try:
            self.sock.connect( (host, port) )
            full_url = "GET " + url + " HTTP/1.0\r\n\r\n"
            cmd = full_url.encode()
            self.sock.send(cmd)

            data_str = ""
            while True:
                data = self.sock.recv(512)
                if len(data) < 1: break
                decoded = [l for l in data.decode().split("\r\n") if( ":" not in l and "HTTP" not in l)]
                data_str = data_str + "".join(decoded)
            return self.strip_cr_lf(data_str)
        finally:
            self.sock.close()


