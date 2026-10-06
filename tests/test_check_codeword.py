from lib.check_codeword import *

def test_correct_codeword_lets_you_in():
    result = check_codeword("horse")
    assert result == "Correct! Come in."
def test_correct_codeword_says_close():
    result = check_codeword("house")
    assert result == "Close, but nope."
def test_correct_codeword_is_wrong():
    result = check_codeword("cat")
    assert result == "WRONG!"