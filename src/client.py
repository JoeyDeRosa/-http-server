"""This file is the client module of the CF 401 Python HTTP-Server assignment."""
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import socket


def client(message=sys.argv[1]):
    """Send given message to server and recover any reply."""
    infos = socket.getaddrinfo('127.0.0.1', 5003)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]

    clnt = socket.socket(*stream_info[:3])
    clnt.connect(stream_info[-1])

    print("Sending: ", message)
    if type(message) == str:
        message = message.encode('utf8')
    clnt.sendall(message)

    buffer_length = 10
    msg_reply = b''

    while True:
        part = clnt.recv(buffer_length)
        msg_reply += part
        if msg_reply[-4:] == b"\r\n\r\n" or msg_reply[-8:] == b"\\r\\n\\r\\n":
                    break

    clnt.close()
    # reply_check = msg_reply.split('\r\n')
    return msg_reply.decode('utf-8')


if __name__ == "__main__":
    client(sys.argv[1])
