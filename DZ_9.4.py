class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'\nАвтомобиль {self.name} начал движение.'

    def stop(self):
        return f'\nАвтомоблиь {self.name} остановился.'

    def turn(self, direction):
        return f'\nАвтомоблиь {self.name} повернул {direction}'

    def show_speed(self):
        return f'\nВаша скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВаша скорость выше допустимой! Ваша скорость {self.speed}'
        else:
            return f'Скорость {self.name} допустимая'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВаша скорость выше допустимой! Ваша скорость {self.speed}'
        else:
            return f'Скорость {self.name} допустимая'


class PoliceCar(Car):
    pass


town = TownCar('BMW', 70, 'черный', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('Audi', 170, 'красный', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('VAZ', 30, 'баклажан', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('Scoda', 100, 'белая', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())