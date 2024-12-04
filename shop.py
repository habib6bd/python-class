class Shop:
    cart = []
    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)

mehjabeen = Shop('Mehjabeen')
mehjabeen.add_to_cart('shoes')
mehjabeen.add_to_cart('phone')
print(mehjabeen.cart)

nisho = Shop('Nisho')
nisho.add_to_cart('watch')
nisho.add_to_cart('cap')
print(nisho.cart)