import pytest


class Employee:
    def __init__(self, name, lastname, wage):
        self.name = name
        self.lastname = lastname
        self.wage = wage
        self.registered_time = 0

    def register_time(self, hours):
        if hours > 24:
            raise ValueError
        self.registered_time += hours

    def pay_salary(self):
        if self.registered_time <= 8:
            payment = self.registered_time * self.wage
        else:
            normal_hours = 8
            overhours = self.registered_time - 8
            payment = normal_hours * self.wage + overhours * self.wage * 2
        self.registered_time = 0
        return payment


def test_employee_initialization():
    employee = Employee("Jan", "Nowak", 100)
    employee.name == "Jan"
    employee.lastname == "Nowak"
    employee.wage = 100


def test_register_time():
    employee = Employee("Jan", "Nowak", 100)
    employee.register_time(5)
    assert employee.registered_time == 5


def test_register_time_and_pay_salary_normal_hours():
    employee = Employee("Jan", "Nowak", 100)
    employee.register_time(5)
    assert employee.pay_salary() == 500
    assert employee.pay_salary() == 0


def test_register_time_and_pay_salary_overdue_hours():
    employee = Employee("Jan", "Nowak", 100)
    employee.register_time(10)
    assert employee.pay_salary() == 1200


def test_many_registrations_one_payment_overdue_hours():
    employee = Employee("Jan", "Nowak", 100)
    employee.register_time(5)
    employee.register_time(5)
    assert employee.pay_salary() == 1200


def test_value_error():
    employee = Employee("Jan", "Nowak", 100)
    with pytest.raises(ValueError) as e:
        employee.register_time(25)


"""
>>> employee = Employee('Jan', 'Nowak', 100.0)
>>> employee.register_time(5)
>>> employee.register_time(5)
>>> employee.pay_salary()
1200.0
>>> employee.pay_salary()
0.0
>>> employee.register_time(10)
>>> employee.pay_salary()
1200.0
>>> employee.register_time(25)
ValueError

"""