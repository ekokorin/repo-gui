class Road:
    def __init__(self, _lenght, _wigth, thickness):
        self._lenght = _lenght
        self._width = _wigth
        self.thickness = thickness

    def weight(self):
        print(f' Вес асфальта дороги шириной {self._lenght}м, длиной {self._width}м, толщиной {self.thickness}см '
              f'составляет {self._lenght * self._width * self.thickness * 25 / 1000} тонн')


my_road = Road(20, 1553, 5)
my_road.weight()
