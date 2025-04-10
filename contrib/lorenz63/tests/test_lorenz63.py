"""tests for contribution lorenz63"""

from contrib.lorenz63.lorenz63 import hello_world

def test_hello_world():
    assert hello_world() == "Hello, World!"
