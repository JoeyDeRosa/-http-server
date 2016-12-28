"""Server for Echo server assignment."""

from __future__ import print_function
import socket
import os


def server():
    port = 5001
    address = ('127.0.0.1', port)
    serv.bind(address)

    serv.listen(1)
    print("Listening on: ", port)

    while True:
        conn, addr = serv.accept()
        try:
           req_result = "500"
            req_string = u''
            buffer_length = 10

            while True:
                part = socket.recv(buffer_length)
                req_string += part.decode('utf-8')
                if req_string[-4:] == u"\r\n\r\n" or req_string[-8:] == u"\\r\\n\\r\\n":
                    break

            if "\\r\\n" in req_string:
                req_string = req_string.replace("\\r\\n", "\r\n")

            print("Testing, ", req_string)
            req_result = parse_request(req_string)
            if len(req_result) < 3:
                conn.sendall(response_ok(req_result))
                print("Reply OK")
            else:
                conn.sendall(response_err(req_result))
                print("Reply error")

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
    print(test_string)
    try:
        test_line = test_string.split('\r\n')
        test_request = test_line[0].split(' ')
        test_body = test_line[1].split(' ')
        print("Test line: ", test_line)
        print("Test Request: ", test_request)
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
    abs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), uri[1:])
    try:
        c_type = mimetypes.guess_type(abs_path)[0]
        if not uri.startswith('/allowed') or '/..' in uri:
            # Check for security - only allow access to one folder.
            print("403")
            return "403"
        elif c_type is None:
            lst = os.listdir(abs_path)
            body = '<ul>\n'
            for item in lst:
                body += '<li>' + item + '</li>\n'
            body += '</ul>\n'
            return ('text/html', body.encode('utf-8'))
        elif 'text' in c_type:
            f = open(abs_path, 'r')
            body = f.read()
            f.close()
            return (c_type, body.encode('utf-8'))
        elif 'image' in c_type:
            f = open(abs_path, 'rb')
            img = f.read()
            f.close()
            return (c_type, img)
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

    reply = "HTTP/1.1 {0} {1}\r\nContent-Type: text/plain\r\n\r\n{2}\r\n\r\n".format(err, err_dict[err][0], err_dict[err][1])
    return reply.encode('utf-8')


def response_ok(content):
    """Return formatted 200 OK HTTP response as byte string."""
    content_type, body = content
    try:
        content_length = len(body.encode('utf-8'))
    except AttributeError:
        content_length = len(body)
    reply = b"HTTP/1.1 200 OK\r\nContent-Type: " + content_type.encode('utf-8') + b"\r\nContent-Length: " + str(content_length).encode('utf-8') + b"\r\n" + body + b"\r\n\r\n"
    return reply

if __name__ == "__main__":
    server()
