from lib.string_builder import *

def test_string_is_clear():
    builder = StringBuilder()
    assert builder.output() == ""