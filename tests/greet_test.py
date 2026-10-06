from lib.greet import *

def test_greet_returns_hello_name():
    result = greet("Jordan")
    assert result == "Hello, Jordan!"