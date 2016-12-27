"""This module tests the client and server modules for the CF 401 Python HTTP-Server assignment."""

import pytest

GOOD_REQ = u"GET /allowed HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
BAD_REQs = [
    u"GOT /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n",
    u"GET /index.html HTTP/0.1\r\nHost: www.example.com\r\n\r\n",
    u"GET index.html HTTP/0.1\r\nHost: www.example.com\r\n\r\n",
    u"GET index.html\r\nHost: www.example.com\r\n\r\n",
    u"GET index.html HTTP/0.1\r\n\r\n\r\n",
    u"GET /index.html HTTP/1.1\r\nHst: www.example.com\r\n\r\n",
    u"GET HTTP/1.1 /index.html\r\nHost: www.example.com\r\n\r\n",
]


FILE_REQ = [
    u"GET /allowed/sample.txt HTTP/1.1\r\nHost: localhost\r\n\r\n",
    u"GET /allowed/awesome.png HTTP/1.1\r\nHost: localhost\r\n\r\n",
]

GOOD_DIR_REQ = u"GET /allowed HTTP/1.1\r\nHost: localhost\r\n\r\n"

BAD_DIR_REQ = [
    u"GET /../src HTTP/1.1\r\nHost: localhost\r\n\r\n",
    u"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n",
]

RESOLVE_URI_GOOD_TESTS = [
    ("/allowed", tuple),
    ("/allowed/sample.txt", tuple),
    ("/allowed/awesome.png", tuple),
]

RESOLVE_URI_BAD_TESTS = [
    ("/..", "403"),
    ("/allowed?txt.txt", "404"),
]

RESPONSE_ERR = [
    (u"500", b"HTTP/1.1 500 Internal Server Error\r\nContent-Type: text/plain\r\n\r\nInvalid HTTP request.\r\n\r\n"),
    (u"404", b"HTTP/1.1 404 File Not Found\r\nContent-Type: text/plain\r\n\r\nThat resource does not exist.\r\n\r\n"),
    (u"403", b"HTTP/1.1 403 Forbidden\r\nContent-Type: text/plain\r\n\r\nAccess not allowed.\r\n\r\n"),
    (u"400", b"HTTP/1.1 400 Bad Request\r\nContent-Type: text/plain\r\n\r\nThe request could not be understood by the server.\r\n\r\n"),
]

RESPONSE_OK = [
    (("text/plain", b"TEST"), b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 4\r\n\r\nTEST\r\n\r\n")
]


def test_parse_request_good_req():
    """Test parse_request with a properly formatted HTTP message."""
    from server import parse_request
    assert parse_request(GOOD_REQ)[0] == 'text/html'


@pytest.mark.parametrize("req", BAD_REQs)
def test_parse_request_bad_req_400(req):
    """Test test_request() witih an improperly formatted HTTP message."""
    from server import parse_request
    assert parse_request(req) == "400"


@pytest.mark.parametrize("req", FILE_REQ)
def test_response_ok(req):
    """Test ok response."""
    from client import client
    assert b'200' == client(req)[9:12]


@pytest.mark.parametrize("req", BAD_REQs)
def test_response_err(req):
    """Test response err."""
    from client import client
    assert b'400' == client(req)[9:12]


def test_response_dir():
    """Test response for a directory."""
    from client import client
    assert client(GOOD_DIR_REQ)[17:40] == b"Content-Type: text/html"


def test_response_txt():
    """Test response for text file."""
    from client import client
    assert client(FILE_REQ[0])[17:41] == b"Content-Type: text/plain"


def test_response_img():
    """Test response for img."""
    from client import client
    assert client(FILE_REQ[1])[17:40] == b'Content-Type: image/png'


@pytest.mark.parametrize("uri, result", RESOLVE_URI_GOOD_TESTS)
def test_resolve_uri_good(uri, result):
    """Test that resolve_uri returns a tuple."""
    from server import resolve_uri
    assert type(resolve_uri(uri)) is result


@pytest.mark.parametrize("uri, result", RESOLVE_URI_BAD_TESTS)
def test_resolve_uri_bad(uri, result):
    """Test that resolve_uri returns an error code."""
    from server import resolve_uri
    assert resolve_uri(uri) is result


@pytest.mark.parametrize("err, result", RESPONSE_ERR)
def test_response_err_format(err, result):
    """Test that response error returns a correctly formatted response for each possible error."""
    from server import response_err
    assert response_err(err) == result


def test_response_ok_format():
    """Test that the response_ok method returns a correctly formatted response."""
    from server import response_ok
    assert response_ok(RESPONSE_OK[0][0]) == RESPONSE_OK[0][1]
