from src.generators import filter_by_currency


def test_filter_by_currency():
    usd_transactions = filter_by_currency(, 'currency')
    assert next(usd_transactions) == 939719570
    assert next(usd_transactions) == 142264268
    assert next(usd_transactions) == 895315941