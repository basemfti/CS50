from bank import value

def test_bes():
    assert value("hello")==0
    assert value("How you doing?")==20
    assert value("What's happening?")==100
    assert value("")==100

