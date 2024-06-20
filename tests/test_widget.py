import pytest
from src.widget import get_data, mask_account_card


def test_mask_account_card(number_for_file_widget):
    assert mask_account_card("Visa 1245123412341234") == number_for_file_widget

    with pytest.raises(TypeError):
        assert mask_account_card(None)

    with pytest.raises(TypeError):
        mask_account_card(not str)



def test_mask_account(number_account_for_file_widget):
    assert mask_account_card("Счет 12246578657898764356") == number_account_for_file_widget


def test_get_data(data):
    assert get_data("2018-07-11T02:26:18.671407") == data
