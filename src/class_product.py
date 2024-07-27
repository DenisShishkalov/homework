class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == '__main__':
    product1 = Product('Купить помидоры', "Помидоры для салата", 180.5, 15)
    product2 = Product('Купить огурцы', "Огурцы для салата", 90, 30)
    product3 = Product('Купить лук', "Лук для салата", 40, 3)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)
