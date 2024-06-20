import pytest

@pytest.fixture
def data():
    return "11.07.2018"


@pytest.fixture
def number_card():
    return 'Visa 1245 23** **** 1234'


@pytest.fixture
def number_account():
    return 'Счет **4356'
