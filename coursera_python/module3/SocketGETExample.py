import socket
from bs4 import BeautifulSoup


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
        sock.shutdown()
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
            self.sock.shutdown()
            self.sock.close()


def get_url_passing_sock(self, host, port, sock, url):
    try:
        sock.connect( (host, port) )
        full_url = "GET " + url + " HTTP/1.0\r\n\r\n"
        cmd = full_url.encode()
        sock.send(cmd)

        data_str = ""
        while True:
            data = sock.recv(512)
            if len(data) < 1: break
            decoded = [l for l in data.decode().split("\r\n") if( ":" not in l and "HTTP" not in l)]
            data_str = data_str + "".join(decoded)
        return strip_cr_lf(data_str)
    finally:
        self.sock.shutdown()
        self.sock.close()


def get_url_using_bs4(ulib, url):
    html = ulib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    span_text_sum = 0
    for i in soup('span'):
        span_text_sum = span_text_sum + int(i.text)
    return span_text_sum


def crawl_hrefs(url, number_of_cycles, position_in_list):
    import urllib.request, urllib.error
    text = None
    current_url = url
    position_in_list = position_in_list - 1
    for i in range(number_of_cycles):
        html = urllib.request.urlopen( current_url ).read()
        soup = BeautifulSoup(html, 'html.parser')
        href_tags = soup('a')
        text = href_tags[position_in_list].text
        current_url = href_tags[position_in_list].get('href', None)
    return text
