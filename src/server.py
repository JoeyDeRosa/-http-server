"""Server for Echo server assignment."""
# encoding: utf-8

import socket


def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    serv.bind(address)

    serv.listen(1)

    while True:
        conn, addr = serv.accept()
        try:
            buffer_length = 10
            echo = u''
            while echo[-2:] != u"\r\n":
                part = conn.recv(buffer_length)
                echo += part.decode('utf8')
                print("Received: ", part)

            print("Sending: ", echo)
            conn.sendall(echo.encode('utf8'))
            print('waiting')
            conn.close()

        except KeyboardInterrupt:
            print("Shutting down server.")
            break
    conn.close()
    serv.close()

server()

def response_err():


def response_ok():