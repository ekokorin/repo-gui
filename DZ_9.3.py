class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname, self.position)

    def get_total_income(self):
        print(self._income['wage']+self._income['wage']*self._income['bonus']/100)


work = Position('Иван', 'Иванов', 'токарь', 30000, 20)
work.get_full_name()
work.get_total_income()

