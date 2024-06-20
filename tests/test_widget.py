import pytest
from src.widget import get_data, mask_account_card


def test_mask_account_card(number_card):
    assert mask_account_card("Visa 1245123412341234") == number_card


def test_mask_account(number_account):
    assert mask_account_card("Счет 12246578657898764356") == number_account


def test_get_data(data):
    assert get_data("2018-07-11T02:26:18.671407") == data
