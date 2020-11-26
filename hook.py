#!/usr/bin/env python3


import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer


def delimeter():
    print('========================================================')


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write(resp_data)

        print("\nHeaders:\n{}".format(str(self.headers))[:-2])
        delimeter()

    def do_POST(self):
        self._set_response()
        self.wfile.write(resp_data)

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("\nHeaders:\n{}Body:\n{}".format(
               str(self.headers), post_data.decode('utf-8')))
        delimeter()


def run(server_class=HTTPServer, handler_class=S, ip='0.0.0.0', port=80):
    try:
        serv = server_class((ip, port), handler_class)
    except:
        print('[\x1b[1;31m-\x1b[0m] Can\'t start server')
        exit()

    print('[\x1b[1;32m+\x1b[0m] Server started at {}:{}\n'.format(ip, port))
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass

    serv.server_close()
    print('[\x1b[1;32m+\x1b[0m] Server stopped! Bye!')


def parse():
    parser = argparse.ArgumentParser(description='Simple http get/post hooks')
    data = parser.add_mutually_exclusive_group()
    parser.add_argument('-i', '--ip', metavar='IP', default='0.0.0.0', type=str,
                        help='set server ip (default: 0.0.0.0)')
    parser.add_argument('-p', '--port', metavar='PORT', type=int, default=80,
                        help='set server port (default: 80)')

    data.add_argument('-d', '--data', metavar='TEXT', type=str,
                      default='Hello from D00Movenok',
                      help='specify response data (default: "Hello from D00Movenok")')
    data.add_argument('-f', '--file', metavar='PATH', type=str,
                      help='specify response data from file')
    args = parser.parse_args()

    global resp_data
    if args.file:
        try:
            resp_data = open(args.file, 'rb').read()
        except:
            print('[\x1b[1;31m-\x1b[0m] Can\'t read the file!')
            exit()
    else:
        resp_data = args.data.encode()

    return args.ip, args.port


if __name__ == '__main__':
    ip, port = parse()
    run(ip=ip, port=port)
