"""Server for Echo server assignment."""
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
import socket


def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    port = 5005
    address = ('127.0.0.1', port)
    serv.bind(address)

    serv.listen(1)
    print("Listening on: ", port)

    while True:
        conn, addr = serv.accept()
        try:
            req_string = b''
            buffer_length = 10

            while True:
                part = conn.recv(buffer_length)
                req_string += part
                if len(part) < buffer_length:
                    break

            print("Sending: ", req_string)
            conn.sendall(req_string)

            print('waiting')
            conn.close()

        except KeyboardInterrupt:
            print("Shutting down server.")
            break
    conn.close()
    serv.close()


if __name__ == "__main__":
    server()
