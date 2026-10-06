from lib.counter import *

def test_new_counter_starts_at_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."
