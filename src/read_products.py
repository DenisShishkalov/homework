import json
from src.config import file_transaction_json_product


def read_file_product(products: list[dict]):
    # name1 = [product['name'] for product in products if 'name']
    # description1 = [product['description'] for product in products if 'description']
    # name2 = products['products']['name']
    return products


with open(file_transaction_json_product, encoding='utf-8') as f:
    products = json.load(f)
