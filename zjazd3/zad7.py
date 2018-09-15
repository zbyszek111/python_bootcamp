from zjazd3.zad2_dobry import Employee


class PremiumEmployee(Employee):

    count = 0


    def __init__(self, name='Jan', lastname='Kowalski', wage = 50, bonus = 0):
        super().__init__(name, lastname, wage)
        self.bonus = bonus
        self.__class__.count += 1

    def give_bonus(self, bonus):
        self.bonus += bonus



    def pay_salary(self):
        sal = super(PremiumEmployee, self).pay_salary() # super().pay.salary()
        sal +=self.bonus
        self.bonus = 0
        return sal

    @classmethod # dotyczy tylko klas
    def create_hero(cls):
        return PremiumEmployee('pracownik', 'miesiaca', 0,0)

    @classmethod
    def emp_from_string(cls, str_param):
        list_param = str_param.split(';')
        return PremiumEmployee(list_param[0],list_param[1], int(list_param[2]))

    @classmethod
    def get_count(cls):
        return cls.count

    def say_hello():
        return 'Hello'

def test_import_from_tekst():
    param = 'Henryk;Zdun;50'
    emp = PremiumEmployee.emp_from_string(param)
    assert emp.name == 'Henryk'
    assert emp.lastname == 'Zdun'
    assert emp.wage == 50



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


def test_employee_of_the_month():
    emp = PremiumEmployee.create_hero()
    assert emp.pay_salary() == 0