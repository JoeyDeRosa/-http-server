"""Server for Echo server assignment."""


import socket


def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    serv.bind(address)

    serv.listen(1)

    conn, addr = serv.accept()

    buffer_length = 10
    echo = ''
    while True:
        part = conn.recv(buffer_length)
        echo += part.decode('utf8')
        if len(part) < buffer_length:
            break

    print("Sending: ", echo)
    conn.sendall(echo.encode('utf8'))
    conn.close()
    serv.close()
