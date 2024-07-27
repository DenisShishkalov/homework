def test_category_init(first_category, second_category):
    assert first_category.name == "Samsung Galaxy S23 Ultra"
    assert first_category.description == "256GB, Серый цвет, 200MP камера"
    assert len(first_category.list_product) == 2
