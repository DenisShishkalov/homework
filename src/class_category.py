from src.class_product import Product


class Category:
    name: str
    description: str
    list_product: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, list_product=None):
        self.name = name
        self.description = description
        self.list_product = list_product if list_product else []
        Category.category_count += 1
        Category.product_count += len(list_product) if list_product else 0


if __name__ == '__main__':
    product1 = Product('Купить помидоры', "Помидоры для салата", 180.5, 15)
    product2 = Product('Купить огурцы', "Огурцы для салата", 90, 30)
    product3 = Product('Купить лук', "Лук для салата", 40, 3)

    category = Category('Салат', "Салат домашний из 3 видов овощей", [product1, product2, product3])

    print(category.name)
    print(category.description)
    print(category.list_product)

    print(category.category_count)
    print(category.product_count)
