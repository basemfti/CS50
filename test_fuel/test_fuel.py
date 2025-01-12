from fuel import convert, gauge
import pytest

def test_convert_valid_fraction():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("1/1") == 100

def test_convert_invalid_fraction():
    with pytest.raises(ValueError):
        convert("2/1")  # ValueError because fraction > 1
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # ZeroDivisionError because division by zero

def test_convert_non_integer_input():
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("1/b")
    with pytest.raises(ValueError):
        convert("a/2")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"

if __name__ == "__main__":
    pytest.main()
