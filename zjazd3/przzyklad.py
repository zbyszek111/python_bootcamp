class Product:

    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self.price = price

    @property
    def full_name(self):
        return 'Product:' +self._name

    @property
    def discount_price(self):
        return self.price * 0.8

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if len(value) > 3:
            self._name = value

pr1 =Product(1, 'Bulka', 10)

print(pr1.price)
print(pr1._id)
print(pr1.full_name)
print(pr1.discount_price)

#atrybut jest chroniony za pomoca property

pr1.name = 'ala ma kota'
print(pr1.name)
print(pr1._name)

# zmiana na wartosc niezgodna z polityka jest niemozliwa
pr1.name = 'cos'
print(pr1.name)
print(pr1._name)