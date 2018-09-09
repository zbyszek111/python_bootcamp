class Employee:

    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.registered_time = 0

    def register_time(self, horus):
        self.registered_time += horus

    def pay_salary(self):
        payment = self.registered_time*self.stawka

def test_employee():
    employee = Employee('Jan', 'Nowak', 100)
    employee.imie == 'Jan'
    employee.nazwisko == 'Nowak'
    employee.stawka == 100


def test_register_time_and_pay_salary_normal_hours():
    employee = Employee("Jan", "Nowak", 100)
    employee.register_time(5)
    assert employee.registered_time == 5



