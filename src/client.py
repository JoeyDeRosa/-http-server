"""This file is the client module of the CF 401 Python HTTP-Server assignment."""

import sys
import socket


def client(message):
    """Send given message to server and recover any reply."""
    infos = socket.getaddrinfo('127.0.0.1', 5002)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]

    clnt = socket.socket(*stream_info[:3])
    clnt.connect(stream_info[-1])

    print("Sending: ", message)
    clnt.sendall(message)

    buffer_length = 10
    msg_reply = u''

    while msg_reply[-4:] != u"\r\n\r\n":
        part = clnt.recv(buffer_length)
        msg_reply += part.decode('utf8')

    clnt.close()
    print("Received: ", msg_reply)
    return msg_reply

if __name__ == "__main__":
    client(sys.argv[1])
