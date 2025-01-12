from twttr import shorten

def test_names():
    assert shorten("basem")=="bsm"

def test_spaces():
    assert shorten("")==""

def test_capitalize():
    assert shorten("15")=="15"
    assert shorten("aeiouAEIOU")==""
    assert shorten("?!")=="?!"





