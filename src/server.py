"""Server for Echo server assignment."""
# encoding: utf-8
from __future__ import print_function
import socket


def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5002)
    serv.bind(address)

    serv.listen(1)

    while True:
        conn, addr = serv.accept()
        try:
            req_string = b''
            buffer_length = 10
            while req_string[-4:] != b"\r\n\r\n":
                part = conn.recv(buffer_length)
                req_string += part

            print("Testing, ", req_string)
            try:
                req_resault = parse_request(req_string)
                if req_resault is False:
                    raise ConnectionError('Invalid Request')
                else:
                    conn.sendall(response_ok())
                    conn.sendall(req_resault)
            except ConnectionError:
                conn.sendall(response_err())
            print('waiting')
            conn.shutdown()
            conn.close()

        except KeyboardInterrupt:
            print("Shutting down server.")
            break
    conn.close()
    serv.close()


def parse_request(test_string):
    """Test HTTP requests for valid format."""
    method_list = 'GET'
    end_list = 'HTTP/1.1'
    body_header = 'Host:'
    test_string = test_string.decode('utf8')
    test_line = test_string.split('\r\n')
    print(test_line)
    test_request = test_line[0].split(' ')
    test_body = test_line[1].split(' ')
    print(test_request)
    if test_request[0] is method_list:
        print("bad method")
        return False
    elif str(test_request[1])[0] is not '/':
        print("bad URI")
        return False
    elif test_request[2] is end_list:
        print("bad protocol")
        return False
    elif test_body[0] is body_header:
        print("bad body header")
        return False
    return str(test_request[1]).encode('utf8')


def response_err():
    """Return formatted 500 error HTTP response as byte string."""
    return b"HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/plain\r\n\r\nBAD message\r\n\r\n"


def response_ok():
    """Return formatted 200 OK HTTP response as byte string."""
    return b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\ngreat message\r\n\r\n"


if __name__ == "__main__":
    server()