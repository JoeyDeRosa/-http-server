"""Server for Echo server assignment."""

from __future__ import print_function
import socket
import os
import html


def server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    port = 5001
    address = ('127.0.0.1', port)
    serv.bind(address)

    serv.listen(1)
    print("Listening on: ", port)

    while True:
        conn, addr = serv.accept()
        try:
            req_string = b''
            buffer_length = 10
            while req_string[-8:] != b"\\r\\n\\r\\n":
                part = conn.recv(buffer_length)
                req_string += part
                print("Received: ", part)

            print("Testing, ", req_string)
            try:
                conn.sendall(response_ok(resolve_uri(parse_request(req_string))))
            except TypeError:
                print("Sending Error response.")
                conn.sendall(response_err())

            print('waiting')
            conn.close()

        except KeyboardInterrupt:
            print("Shutting down server.")
            break
    conn.close()
    serv.close()


def parse_request(test_string):
    """Test HTTP requests for valid format."""
    method = 'GET'
    end_list = 'HTTP/1.1'
    body_header = 'Host:'
    try:
        test_string = test_string.decode('utf8')
        test_line = test_string.split('\\r\\n')
        test_request = test_line[0].split(' ')
        test_body = test_line[1].split(' ')
        print(test_request)
        if str(test_request[0]) != method:
            print("bad method")
            raise ValueError
        elif str(test_request[1])[0] != '/':
            print("bad uri")
            raise ValueError
        elif str(test_request[2]) != end_list:
            print("bad proto")
            raise ValueError
        elif str(test_body[0]) != body_header:
            print("bad header")
            raise ValueError
    except ValueError:
        return
    except IndexError:
        return
    else:
        return str(test_request[1]).encode('utf8')


def resolve_uri(uri):
    """Return response body and type as tuple."""
    # if type(uri) is not str:
    #     uri = uri.decode('utf8')
    try:
        if not uri.startswith(u'/allowed'):
            #Check for security - only allow access to one folder.
            print("OUT")
            raise ValueError
        elif uri.endswith(u'.txt'):
            f = open(uri[1:], 'r')
            body = f.read()
            f.close()
            print(body)
            return ('text/plain', body)
        elif uri.endswith(u'.png'):
            f = open(uri[1:], 'rb')
            img = f.read()
            f.close()
            print(img)
            return ('image/png', img)
        else:
            lst = os.listdir(uri[1:])
            body = '<ul>\n'
            for item in lst:
                body += '<li>' + item + '</li>\n'
            body += '</ul>\n'
            print(body)
            return ('text/html', body)
    except ValueError:
        return None


def response_err():
    """Return formatted 500 error HTTP response as byte string."""
    return b"HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/plain\r\n\r\nBAD message\\r\\n\\r\\n"


def response_ok(content):
    """Return formatted 200 OK HTTP response as byte string."""
    content_type, body = content
    content_length = len(body.encode('utf-8'))
    reply = u"HTTP/1.1 200 OK\r\nContent-Type: {0}\r\nContent-Length: {1}\r\n\r\n{2}\r\n\r\n".format(content_type, content_length, body)
    return reply.encode('utf-8')

if __name__ == "__main__":
    server()
