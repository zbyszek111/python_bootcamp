from zjazd3.zad2_dobry import Employee


class PremiumEmployee(Employee):
    def __init__(self, name='Jan', lastname='Kowalski', wage = 500, bonus = 0):
        super().__init__(name, lastname, wage)
        self.bonus = bonus

    def give_bonus(self, bonus):
        self.bonus += bonus



    def pay_salary(self):
        sal = super(PremiumEmployee, self).pay_salary() # super().pay.salary()
        sal +=self.bonus
        self.bonus = 0
        return sal



def test_create():
    emp = PremiumEmployee('Jan', 'Nowak', 100, 2000)
    assert emp.name == 'Jan'
    assert emp.lastname == 'Nowak'
    assert emp.wage == 100
    assert emp.bonus == 2000


def test_register():
    emp = PremiumEmployee('Jan', 'Nowak', 100)
    emp.register_time(5)
    emp.give_bonus(1000)
    emp.give_bonus(400)
    assert emp.bonus == 1400
    assert emp.pay_salary() == 1900
