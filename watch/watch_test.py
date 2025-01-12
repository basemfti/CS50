
import pytest
from watch import parse

def test_valid_embed_urls():
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe src="https://www.youtube.com/embed/abcd1234"></iframe>') == "https://youtu.be/abcd1234"

def test_invalid_embed_urls():
    assert parse('<iframe src="https://www.notyoutube.com/embed/xvFZjo5PgG0"></iframe>') == None
    assert parse('<iframe src="https://youtube.com/embed/"></iframe>') == None
    assert parse('<iframe src="https://www.youtube.com/xvFZjo5PgG0"></iframe>') == None
    assert parse('<iframe width="560" height="315"></iframe>') == None

def test_no_iframe():
    assert parse('<div>Some other HTML content</div>') == None
    assert parse('') == None

