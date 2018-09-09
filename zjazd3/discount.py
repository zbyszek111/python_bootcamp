class Product:

    def __init__(self, id, name, price):
        self.price = price

        self._id = id
        self._name = name
        self._discount = 0

    @property
    def full_name(self):
        return 'Product:' +self._name

    @property
    def name(self):
        return self._name

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self,value):
        if type(value) == float or type(value) == int:
            if 0 <= value <= 0.3:
                self._discount = value

    @discount.deleter
    def discount(self):
        self._discount = 0

    @property
    def discount_price(self):
        return self.price * (1-self._discount)

    @name.setter
    def name(self,value):
        if len(value) > 3:
            self._name = value

pr1 =Product(1, 'Bulka', 10)

print(pr1.price)
print(pr1._id)
print(pr1.full_name)
print(pr1.discount_price)
print(pr1.discount)

#atrybut jest chroniony za pomoca property

pr1.name = 'ala ma kota'
print(pr1.name)
print(pr1._name)
