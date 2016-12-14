"""Server for Echo server assignment."""


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
            while req_string[-2:] != u"\r\n":
                part = conn.recv(buffer_length)
                req_string += part.decode('utf8')
                print("Received: ", part)
            if test_request(req_string):
                response_ok()
                print('waiting')
                conn.close()
            else:
                response_error()

        except KeyboardInterrupt:
            print("Shutting down server.")
            break
    conn.close()
    serv.close()


def test_request(test_string):
    method_list = ['GET', 'POST', 'PUT', 'DELETE']
    end_list = ['HTTP/1.1', 'HTTP/1.0']
    test_line = test_string.split('\r\n')
    test_section = test_line[0].split(' ')
    if test_section[0] not in method_list:
        return False
    elif test_section[1][0] is not '/':
        return False
    elif test_section[2] not in end_list:
        return False
    return True


server()
