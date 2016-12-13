"""Server for Echo server assignment."""


import socket


def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    serv.bind(address)

    serv.listen(1)

    conn, addr = serv.accept()

    while True:
        try:
            buffer_length = 10
            echo = ''
            rec = True
            while rec:
                part = conn.recv(buffer_length)
                echo += part.decode('utf8')
                if len(part) < buffer_length:
                    rec = False
            print("Sending: ", echo)
            conn.sendall(echo.encode('utf8'))
            print('waiting')
            conn, addr = serv.accept()
        except KeyboardInterrupt:
            break
    conn.close()
