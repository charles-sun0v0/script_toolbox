from http.server import BaseHTTPRequestHandler
import socketserver
from io import BytesIO
import cgi
import json
import requests

station_address = "http://127.0.0.1:8080"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

url1 = '/bar'
url2 = '/foo'

class RequestHandler(BaseHTTPRequestHandler):
    cnt = 0
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers('content-type'))

        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        self._set_headers()
        # read the message and convert it into a python dictionary
        length = int(self.headers('content-length'))

        if self.path == url1:
            # send next box
            print("current box response: {MixPalletizeHandler.cnt}")

        elif self.path == url2:
            # print pallet
            print(url2)

        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(bytes(self.path, 'utf-8'))
        self.wfile.write(response.getvalue())


def run_server():
    handler_object = RequestHandler

    PORT = 60001
    my_server = socketserver.TCPServer(("", PORT), handler_object)

    # Star the server
    my_server.serve_forever()


if __name__ == "__main__":
    run_server()
