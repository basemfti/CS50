from um import count

def test_single_um():
    assert count("um") == 1

def test_multiple_um():
    assert count("um, um, um") == 3

def test_um_case_insensitive():
    assert count("Um, uM, UM, um") == 4

def test_um_as_substring():
    assert count("yummy, aluminum") == 0

def test_um_with_punctuation():
    assert count("hello, um... world!") == 1

def test_no_um():
    assert count("hello, world!") == 0

def test_um_at_boundaries():
    assert count("um at the beginning and um at the end um") == 3
