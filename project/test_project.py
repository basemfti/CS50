import pytest
from unittest.mock import patch
from project import show_balance, deposit, withdraw

@pytest.fixture(scope='module')

def test_show_balance(capsys, engine):
    balance = 100
    with patch('project.engine', engine):
        show_balance(balance)
    captured = capsys.readouterr()
    assert "your balance is $100.00" in captured.out

def test_deposit_valid_amount(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '50')
    amount = deposit()
    assert amount == 50

def test_deposit_invalid_amount(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '-10')
    amount = deposit()
    assert amount == 0

def test_withdraw_valid_amount(monkeypatch):
    balance = 100
    monkeypatch.setattr('builtins.input', lambda _: '50')
    amount = withdraw(balance)
    assert amount == 50

def test_withdraw_insufficient_funds(monkeypatch):
    balance = 50
    monkeypatch.setattr('builtins.input', lambda _: '100')
    amount = withdraw(balance)
    assert amount == 0

def test_withdraw_invalid_amount(monkeypatch):
    balance = 100
    monkeypatch.setattr('builtins.input', lambda _: '-10')
    amount = withdraw(balance)
    assert amount == 0
