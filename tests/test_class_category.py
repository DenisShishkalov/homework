def test_category_init(first_category, second_category):
    assert first_category.name == 'Samsung Galaxy S23 Ultra'
    assert first_category.description == "256GB, Серый цвет, 200MP камера"
    assert len(first_category.list_product) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4