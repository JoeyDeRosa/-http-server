"""This file is the client module of the CF 401 Python HTTP-Server assignment."""

import sys
import socket

def client(message):
    """Send given message to server and recover any reply."""
    infos = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]

    clnt = socket.socket(*stream_info[:3])
    clnt.connect(stream_info[-1])

    clnt.sendall(message.encode('utf8'))

    buffer_length = 10
    reply_complete = False
    msg_reply = ""

    while not reply_complete:
        part = clnt.recv(buffer_length)
        msg_reply += part.decode('utf8')
        if len(part) < buffer_length:
            break

    return msg_reply

if __name__ == "__main__":
    client(sys.argv[1])