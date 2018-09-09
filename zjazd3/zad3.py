class ElectricCar:

    def __init__(self, distance):
        self.distance = distance


    def drive(self, kilometry):
        dystans = self.distance - kilometry
        if dystans<= self.distance:
            dystans == 0
        return dystans

    def charge(self):
        self.kilometry = self.distance


def test_car_initial():
    car = ElectricCar(100)
    assert car.drive(50) == 50

def test_charge():
    car = ElectricCar(100)
    car.drive(50)
    car.charge()
    assert car.drive(50) == 50