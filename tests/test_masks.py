import pytest
from src.masks import get_mask_account


def test_get_mask_account_number(number):
    assert get_mask_account(number)


def test_get_mask_account_invalid_len_and_letters():
    with pytest.raises(ValueError):
        get_mask_account('1245fgjdf125326jfgddfgg')


def test_get_mask_account_not_number():
    with pytest.raises(AssertionError):
        get_mask_account("")

# @pytest.mark.parametrize('1335466534'
#                          '109364294093910194')
# def test_get_mask_account_len_number():
#     with pytest.raises(AssertionError):
#         get_mask_account(number)
