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


@pytest.mark.parametrize("req", TEST_PARAMS)
def test_test_request_any_req(req):
    """Functional test for a variety of mesaages."""
    from client import client
    assert client(req) == req
