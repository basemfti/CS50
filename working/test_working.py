import pytest
from working import convert

def test_valid_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("1:00 PM to 1:00 AM") == "13:00 to 01:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

def test_invalid_times():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("9:00AMto5:00PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 5 PM tomorrow")

def test_edge_cases():
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("12:01 AM to 11:59 PM") == "00:01 to 23:59"

if __name__ == "__main__":
    pytest.main()
