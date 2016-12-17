"""Server for Echo server assignment."""

from __future__ import print_function
import socket
import os


def g_server(socket, address):

    while True:
        try:
            req_result = "500"
            req_string = b''
            buffer_length = 10
            while req_string[-8:] != b"\\r\\n\\r\\n":
                part = socket.recv(buffer_length)
                req_string += part
                print("Received: ", part)

            print("Testing, ", req_string)

            req_result = parse_request(req_string)
            if len(req_result) < 3:
                socket.sendall(response_ok(req_result))
            else:
                socket.sendall(response_err(req_result))

            print('waiting')
            socket.close()

        except KeyboardInterrupt:
            print("Shutting down server.")
            break


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
            return "400"
        elif str(test_request[1])[0] != '/':
            print("bad uri")
            return "400"
        elif str(test_request[2]) != end_list:
            print("bad proto")
            return "400"
        elif str(test_body[0]) != body_header:
            print("bad header")
            return "400"
    except IndexError:
        return "400"
    else:
        return resolve_uri(str(test_request[1]))


def resolve_uri(uri):
    """Return response body and type as tuple."""
    # if type(uri) is not str:
    #     uri = uri.decode('utf8')
    abs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), uri[1:])
    try:
        if not uri.startswith('/allowed') or '/..' in uri:
            #Check for security - only allow access to one folder.
            print("403")
            return "403"
        elif uri.endswith(u'.txt'):
            f = open(abs_path, 'r')
            body = f.read()
            f.close()
            print(body)
            return ('text/plain', body)
        elif uri.endswith(u'.png') or uri.endswith(u'.jpeg') or uri.endswith(u'.bmp'):
            f = open(abs_path, 'rb')
            img = f.read()
            f.close()
            print(img[:100])
            return ('image/png', img)
        else:
            lst = os.listdir(abs_path)
            body = '<ul>\n'
            for item in lst:
                body += '<li>' + item + '</li>\n'
            body += '</ul>\n'
            print(body)
            return ('text/html', body)
    except IOError:
        return "404"


def response_err(err):
    """Return formatted 500 error HTTP response as byte string."""
    if type(err) != str:
        err = err.decode('utf-8')
    err_dict = {
        "500": ("Internal Server Error", "Invalid HTTP request."),
        "404": ("File Not Found", "That resource does not exist."),
        "403": ("Forbidden", "Access not allowed."),
        "400": ("Bad Request", "The request could not be understood by the server.")
    }

    reply = "HTTP/1.1 {0} {1}\r\nContent-Type: text/plain\r\n\r\n{2}\\r\\n\\r\\n".format(err, err_dict[err][0], err_dict[err][1])
    return reply.encode('utf-8')


def response_ok(content):
    """Return formatted 200 OK HTTP response as byte string."""
    content_type, body = content
    try:
        content_length = len(body.encode('utf-8'))
    except AttributeError:
        content_length = len(body)
    reply = u"HTTP/1.1 200 OK\r\nContent-Type: {0}\r\nContent-Length: {1}\r\n\r\n{2}\\r\\n\\r\\n".format(content_type, content_length, body)
    return reply.encode('utf-8')

if __name__ == "__main__":
    from gevent.server import StreamServer
    from gevent.monkey import patch_all
    patch_all()
    port = 5000
    server = StreamServer(('127.0.0.1', port), g_server)
    print('Starting server on port ', port)
    server.serve_forever()
