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

            req_string = req_string.decode('utf-8')
            if "\\r\\n" in req_string:
                req_string = req_string.replace("\\r\\n", "\r\n")

            conn.sendall(response_ok())
            if req_string[0] == '`':
                print("Received: \n", req_string[1:])
            else:
                print("Received: \n", req_string)

            print('waiting')
            conn.close()

        except KeyboardInterrupt:
            print("Shutting down server.")
            break
    conn.close()
    serv.close()


def response_err(err):
    """Return formatted 500 error HTTP response as byte string."""
    if type(err) != str:
        err = err.decode('utf-8')
    err_dict = {
        "500": ("Internal Server Error", "Invalid HTTP request."),
        "404": ("File Not Found", "That resource does not exist."),
        "403": ("Forbidden", "Access not allowed."),
        "400": ("Bad Request", "The request could not be understood by the server.")
    }

    reply = "HTTP/1.1 {0} {1}\r\nContent-Type: text/plain\r\n\r\n{2}\r\n\r\n".format(err, err_dict[err][0], err_dict[err][1])
    return reply.encode('utf-8')


def response_ok():
    """Return formatted 200 OK HTTP response as byte string."""
    return b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 4\r\n\r\nTEST\r\n\r\n"

if __name__ == "__main__":
    server()
