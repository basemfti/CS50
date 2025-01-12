from plates import is_valid

def test_bes():
    assert is_valid("CS50")==True
    assert is_valid("AER")==True
    assert is_valid("AERfdfsd")==False
    assert is_valid("A")==False
    assert is_valid("ATGB0")==False
    assert is_valid("66DF")==False
    assert is_valid("45553")==False
    assert is_valid("45553")==False
    assert is_valid("ac23!") == False
    assert is_valid("a32") == False









