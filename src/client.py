# -*- coding: utf-8 -*-
"""This file is the client module of the CF 401 Python HTTP-Server assignment."""

from __future__ import unicode_literals
from __future__ import print_function
import sys
import socket


def client(message):
    """Send given message to server and recover any reply."""
    infos = socket.getaddrinfo('127.0.0.1', 5005)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]

    clnt = socket.socket(*stream_info[:3])
    clnt.connect(stream_info[-1])

    buffer_length = 10
    msg_reply = b''

    print("Sending: ", message)
    # if type(message) == str:
    message = message.encode('utf8')
    if len(message) % buffer_length == 0:
        message = b"`" + message

    clnt.sendall(message)

    while True:
        part = clnt.recv(buffer_length)
        msg_reply += part
        if len(part) < buffer_length:
            break

    msg_reply = msg_reply.decode('utf-8')
    if msg_reply[0] == '`':
        msg_reply = msg_reply[1:]

    clnt.close()
    print("Received: ", msg_reply)
    return msg_reply


def main():
    """Pass system arguments to client."""
    client(sys.argv[1])


if __name__ == "__main__":
    client(sys.argv[1])
