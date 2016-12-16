"""This modulet tests the client and server modules for the CF 401 Python HTTP-Server assignment."""

import pytest

# Test the following:
# messages shorter than one buffer in length
# messages longer than several buffers in length
# messages that are an exact multiple of one buffer in length
# messages containing non-ascii characters

# def test_client_short():
#     """Test with message shorter than one buffer length."""
#     from client import client
#     test_msg = "twerp"
#     return client(test_msg) == u"twerp"

# def test_client_long():
#     """Test with message longer than several buffers in length."""
#     from client import client
#     test_msg = "This is a very long test message."
#     return client(test_msg) == test_msg

# def test_client_exact_buffer():
#     """Test messages that are an exact multiple of one buffer in length."""
#     from client import client
#     test_msg = "abcdefghij"
#     return client(test_msg) == test_msg


# def test_client_non_ASCII():
#     """Test messages that contain non ASCII characters."""
#     from client import client

"""BEGIN TESTS FOR STEP1 ASSIGNMENT"""

# GET /index.html HTTP/1.1<CRLF>
# Host: www.example.com<CRLF>
# <CRLF>

GOOD_REQ = u"GET /allowed HTTP/1.1\\r\\nHost: www.example.com\\r\\n\\r\\n"
BAD_REQs = [
    b"GOT /index.html HTTP/1.1\\r\\nHost: www.example.com\\r\\n\\r\\n",
    b"GET /index.html HTTP/0.1\\r\\nHost: www.example.com\\r\\n\\r\\n",
    b"GET index.html HTTP/0.1\\r\\nHost: www.example.com\\r\\n\\r\\n",
]


FILE_REQ = [
    u"GET /allowed/sample.txt HTTP/1.1\\r\\nHost: localhost\\r\\n\\r\\n",
    u"GET /allowed/awesome.png HTTP/1.1\\r\\nHost: localhost\\r\\n\\r\\n",
]

GOOD_DIR_REQ = u"GET /allowed HTTP/1.1\\r\\nHost: localhost\\r\\n\\r\\n"

BAD_DIR_REQ = [
    u"GET /../src HTTP/1.1\\r\\nHost: localhost\\r\\n\\r\\n",
    u"GET / HTTP/1.1\\r\\nHost: localhost\\r\\n\\r\\n",
]

RESOLVE_URI_TESTS = [
    ("/allowed", tuple),
    ("/allowed/sample.txt", tuple),
    ("/allowed/awesome.png", tuple),
    ("/allowed/txt.txt", "404"),
    ("/..", "403"),
]


def test_parse_request_good_req():
    """Test parse_request with a properly formatted HTTP message."""
    from server import parse_request
    assert parse_request(GOOD_REQ.encode('utf-8'))[0] == 'text/html'


@pytest.mark.parametrize("req", BAD_REQs)
def test_parse_request_bad_req_400(req):
    """Test test_request() witih an improperly formatted HTTP message."""
    from server import parse_request
    assert parse_request(req) == "400"


@pytest.mark.parametrize("req", FILE_REQ)
def test_response_ok(req):
    """Test ok response."""
    from client import client
    assert '200' == client(req)[0][9:12]


@pytest.mark.parametrize("req", BAD_REQs)
def test_response_err(req):
    """Test response err."""
    from client import client
    assert '500' == client(req)[0][9:12]


def test_response_dir():
    """Test response for a directory."""
    from client import client
    assert client(GOOD_DIR_REQ)[1] == "Content-Type: text/html"


def test_response_txt():
    """Test response for text file."""
    from client import client
    assert client(FILE_REQ[0])[1] == "Content-Type: text/plain"


def test_response_img():
    """Test response for img."""
    from client import client
    assert client(FILE_REQ[1])[1] == 'Content-Type: image/png'


@pytest.mark.parametrize("uri, result", RESOLVE_URI_TESTS)
def test_resolve_uri(uri, result):
    """Test resolve_uri function."""
    from server import resolve_uri
    assert resolve_uri(uri) is result