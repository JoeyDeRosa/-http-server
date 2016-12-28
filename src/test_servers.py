"""This modulet tests the client and server modules for the CF 401 Python HTTP-Server assignment."""

import pytest


"""BEGIN TESTS FOR STEP1 ASSIGNMENT"""

# GET /index.html HTTP/1.1<CRLF>
# Host: www.example.com<CRLF>
# <CRLF>

GOOD_REQ = u"GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
BAD_REQs = [
    u"GOT /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n",
    u"GET /index.html HTTP/0.1\r\nHost: www.example.com\r\n\r\n",
    u"GET index.html HTTP/0.1\r\nHost: www.example.com\r\n\r\n",
]


def test_parse_request_good_req():
    """Test test_request() with a properly formatted HTTP message."""
    from server import parse_request
    assert parse_request(GOOD_REQ) == "/index.html"


@pytest.mark.parametrize("req", BAD_REQs)
def test_parse_request_bad_req(req):
    """Test test_requrest() witih an improperly formatted HTTP message."""
    from server import parse_request
    assert parse_request(req) == "400"


def test_response_ok():
    """Test ok response."""
    from client import client
    assert '200' == client(GOOD_REQ)[9:12]


@pytest.mark.parametrize("req", BAD_REQs)
def test_response_err(req):
    """Test response err."""
    from client import client
    assert '400' == client(req)[9:12]
