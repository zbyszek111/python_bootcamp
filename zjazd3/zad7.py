from zjazd3.zad2_dobry import Employee


class PremiumEmployee(Employee):
    def __init__(self, name, lastname, wage):
        super().__init__(name, lastname, wage)
        self.bonus = None

    pass


def test_create():
    emp = PremiumEmployee('Jan', 'Nowak', 100)
    assert emp.name == 'Jan'
    assert emp.lastname == 'Nowak'
    assert emp.wage == 100
    assert emp.bonus == 0


def test_register():
    emp = PremiumEmployee('Jan', 'Nowak', 100)
    emp.register_time(5)
    emp.give_bonus(1000)
    assert emp.pay_salary() == 1500
