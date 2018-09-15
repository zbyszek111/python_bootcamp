# Stwórz klasę Animal, która ma atrybuty name i age, oraz metodę sound
# >>> animal = Animal("Strange something", 1000)
# >>> animal.name
# "Strange something"
# >>> animal.age
# 1000
# >>> animal.sound()
# "kncok kncok"
# Stwórz klasy Dog i Cat, które dziedziczą po Animal i przeciążają metodę sound tak, że:
# >>> cat = Cat("Albert", 5)
# >>> dog = Dog("Nina", 6)
# >>> dog.sound()
# "how how"
# >>> cat.sound()
# "... (sorry - that's cat!)"
# Przeciaż operator >  tak by, można było porównywać wiek:
# >>> cat > dog
# True
# >>> dog > animal
# False


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sound = "knock knock"

    def sound(self):
        return self.sound


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sound = "... (sorry - that's cat!)"

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sound = "how how"

def test_animal():
    animal = Animal("Strange something", 1000)
    assert animal.name == "Strange something"
    assert animal.age == 1000
    assert animal.sound == "knock knock"


def test_dog():
    dog = Dog("Nina", 6)
    assert dog.sound == "how how"
    assert dog.age == 6

def test_cat():
    cat = Cat("Nina", 6)
    assert cat.sound == "... (sorry - that's cat!)"

def test_compare_cat_dog_age():
    cat = Cat("Nina", 6)
    dog = Dog("Nina", 1)
    assert cat.age > dog.age == True