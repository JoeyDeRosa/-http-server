"""Server for Echo server assignment."""


import socket


def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    server.bind(address)

    server.listen(1)

    conn, addr = server.accept()

    buffer_length = 10
    echo = ''
    while True:
        echo += conn.recv(buffer_length).decode('utf8')
        if len(conn.recv(buffer_length)) < buffer_length:
            break

    conn.sendall(echo.encode('utf8'))
