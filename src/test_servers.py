"""This modulet tests the client and server modules for the CF 401 Python HTTP-Server assignment."""

# Test the following:
# messages shorter than one buffer in length
# messages longer than several buffers in length
# messages that are an exact multiple of one buffer in length
# messages containing non-ascii characters

def test_client_short():
    """Test with message shorter than one buffer length."""
    from client import client
    test_msg = "twerp"
    assert client(test_msg) == u"twerp"

def test_client_long():
    """Test with message longer than several buffers in length."""
    from client import client
    test_msg = "This is a very long test message."
    assert client(test_msg) == test_msg

def test_client_exact_buffer():
    """Test messages that are an exact multiple of one buffer in length."""
    from client import client


def test_client_non_ASCII():
    """Test messages that contain non ASCII characters."""
    from client import client
    
