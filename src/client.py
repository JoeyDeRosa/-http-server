"""This file is the client module of the CF 401 Python HTTP-Server assignment."""

import sys
import socket


def client(message):
    """Send given message to server and recover any reply."""
    infos = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]

    clnt = socket.socket(*stream_info[:3])
    clnt.connect(stream_info[-1])

    print("Sending: ", message)
    if type(message) == str:
        message = message.encode('utf8')
    clnt.sendall(message)

    buffer_length = 10
    msg_reply = b''

    while msg_reply[-8:] != b"\\r\\n\\r\\n":
        part = clnt.recv(buffer_length)
        msg_reply += part
    clnt.close()
    display = msg_reply.decode('utf8')
    reply_check = split_reply(display)
    print("Received: ", display)
    return reply_check


def split_reply(reply):
    return reply.split('\r\n')


if __name__ == "__main__":
    client(sys.argv[1])
