class Store:
    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, product, price):
        self.products[product] = price

    def get_price(self, product):
        return self.products.get(product, None)


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = {}

    def add_to_cart(self, store, product, quantity):
        price = store.get_price(product)
        if price is not None:
            self.cart[product] = (quantity, price)

    def checkout(self):
        total = sum(quantity * price for quantity, price in self.cart.values())
        self.cart.clear()
        return total
