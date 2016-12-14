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
            req_string = u''
            buffer_length = 10
            while req_string[-4:] != u"\r\n\r\n":
                part = conn.recv(buffer_length)
                req_string += part.decode('utf8')
                print("Received: ", part)
            if test_request(req_string):
                conn.sendall(response_ok())
            else:
                conn.sendall(response_err())

            print('waiting')
            conn.close()

        except KeyboardInterrupt:
            print("Shutting down server.")
            break
    conn.close()
    serv.close()


def test_request(test_string):
    """Test HTTP requests for valid format."""
    method_list = ['GET', 'POST', 'PUT', 'DELETE']
    end_list = ['HTTP/1.1', 'HTTP/1.0']
    test_string = test_string.decode('utf8')
    test_line = test_string.split('\r\n')
    print(test_line)
    test_section = test_line[0].split(' ')
    print(test_section)
    if test_section[0] not in method_list:
        print("bad method")
        return False
    elif test_section[1][0] is not '/':
        print("bad URI")
        return False
    elif test_section[2] not in end_list:
        print("bad protocol")
        return False
    return True


def response_err():
    """Return formatted 500 error HTTP response as byte string."""
    return b"HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/plain\r\n\r\nBAD message\r\n"

# HTTP/1.1 200 OK
# Content-Type: text/plain
# <CRLF>
# this is a pretty minimal response
def response_ok():
    """Return formatted 200 OK HTTP response as byte string."""
    return b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\ngreat message\r\n"
