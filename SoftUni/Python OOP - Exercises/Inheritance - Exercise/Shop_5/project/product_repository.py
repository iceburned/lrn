from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for obj in self.products:
            if obj.name == product_name:
                return obj

    def remove(self, product_name: str):
        product = self.find(product_name)
        if product is not None:
            self.products.remove(product)

    def __repr__(self):
        result = ''
        for obj in self.products:
            result += f'{obj.name}: {obj.quantity}\n'
        return result.strip()

