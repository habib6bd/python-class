class Shop:
    shopping_mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

mehjabeen = Shop('Mehjabeen')
mehjabeen.add_to_cart('shoes')
mehjabeen.add_to_cart('bag')
print(mehjabeen.cart)

nisho = Shop('nisho')
nisho.add_to_cart('watch')
nisho.add_to_cart('moneybag')
print(nisho.cart)
        