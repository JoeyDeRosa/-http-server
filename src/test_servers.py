"""This modulet tests the client and server modules for the CF 401 Python HTTP-Server assignment."""
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest


# buffer length is 10
TEST_PARAMS = [
    "Try this..",
    "This statement is much longer than one buffer length.",
    "This statement £includes non-ASCII §characters.®",
    "Try this..Try this..Try this.."
]


def test_request_good_req():
    """Test test_request() with a properly formatted HTTP message."""
    from server import response_ok
    assert response_ok() == b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 4\r\n\r\nTEST\r\n\r\n"


@pytest.mark.parametrize("req", TEST_PARAMS)
def test_test_request_bad_req(req):
    """Test test_requrest() witih an improperly formatted HTTP message."""
    from client import client
    assert client(req)[9:12] == "200"
