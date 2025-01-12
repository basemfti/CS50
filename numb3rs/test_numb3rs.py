import pytest

from numb3rs import validate

def test_valid_ipv4():
    assert validate("192.168.0.1") == True
    assert validate("10.0.0.1") == True
    assert validate("255.255.255.255") == True

def test_invalid_ipv4():
    assert validate("275.3.6.28") == False
    assert validate("192.168.0.300") == False
    assert validate("192.168.-1.1") == False
    assert validate("192.168.0.0.1") == False
    assert validate("192 .168.0.1") == False
    assert validate("192.168.0.1 ") == False
    assert validate("192.168.0.1/") == False

def test_edge_cases():
    assert validate("") == False
    assert validate("192.168.0") == False
    assert validate("192.168.0.1.1") == False
    assert validate("192.168.0..1") == False
    assert validate("192..0.1.1") == False
