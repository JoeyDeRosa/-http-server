"""Server for Echo server assignment."""


import socket


def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5008)
    serv.bind(address)

    serv.listen(1)

    conn, addr = serv.accept()

    while True:
        try:
            buffer_length = 10
            echo = ''
            rec = True
            while rec:
                try:
                    part = conn.recv(buffer_length)
                    echo += part.decode('utf8')
                    print("Received: ", part)
                except socket.error:
                    rec = False

            print("Sending: ", echo)
            conn.sendall(echo.encode('utf8'))
            print('waiting')
            conn, addr = serv.accept()
        except KeyboardInterrupt:
            print("Shutting down server.")
            break
    conn.close()
    serv.close()

server()