import pytest


@pytest.fixture
def number_for_file_masks():
    return '3234 12** **** 1234'


@pytest.fixture
def number_for_account_for_file_masks():
    return "**7757"


@pytest.fixture
def letter_for_file_masks():
    return 'Введены некорректные данные'


@pytest.fixture
def number_for_file_widget():
    return 'Visa 1245 23** **** 1234'


@pytest.fixture
def number_account_for_file_widget():
    return 'Счет **4356'


@pytest.fixture
def data():
    return "11.07.2018"