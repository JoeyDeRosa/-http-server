"""Server for Echo server assignment."""


import socket


def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5003)
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
                print(type(part.decode('utf8')))
                echo += part.decode('utf8')
                if len(part) < buffer_length or len(part) is 0:
                    rec = False
            if echo[-1] is '~' and (len(echo) - 1) % 10 is 0:
                fix_str = echo[:-1]
                echo = fix_str
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