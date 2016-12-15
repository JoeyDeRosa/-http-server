"""Server for Echo server assignment."""
# encoding: utf-8
from __future__ import print_function
import socket


def server():
    """Simple server to receive and echo messages."""
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    port = 5000
    address = ('127.0.0.1', port)
    serv.bind(address)

    serv.listen(1)
    print("Listening on port: ", port)

    while True:
        conn, addr = serv.accept()
        try:
            req_string = b''
            buffer_length = 10
            while req_string[-4:] != b"\r\n\r\n":
                part = conn.recv(buffer_length)
                req_string += part

            print("Testing, ", req_string)
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
    elif str(test_section[1])[0] is not '/':
        print("bad URI")
        return False
    elif test_section[2] not in end_list:
        print("bad protocol")
        return False
    return True


def response_err():
    """Return formatted 500 error HTTP response as byte string."""
    return b"HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/plain\r\n\r\nBAD message\r\n\r\n"


def response_ok():
    """Return formatted 200 OK HTTP response as byte string."""
    return b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\ngreat message\r\n\r\n"


if __name__ == "__main__":
    server()
