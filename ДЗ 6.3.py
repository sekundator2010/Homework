class Worker:
    def __init__(self, name, surname, position):
        self.name, self.surname, self.position, self._income = name, surname, position, {'wage': 20000, 'bonus' : 5000}
class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудника зовут {self.name, self.surname}')

    def get_total_income(self):
        i, u = self._income['wage'] , self._income['bonus']
        print(f'Доход сотрудника с учётом премии: {i + u}')
pos = Position('Ivan', 'Shorohov', 'manager')
pos.get_full_name()
pos.get_total_income()
