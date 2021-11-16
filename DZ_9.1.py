import time


class TrafficLight:
    __color = ''

    def running(self):

        self.__color = 'красный'
        print(f'Горит {self.__color} цвет.')
        time.sleep(7)

        self.__color = 'желтый'
        print(f'Горит {self.__color} цвет.')
        time.sleep(2)

        self.__color = 'зеленый'
        print(f'Горит {self.__color} цвет.')
        time.sleep(7)

        while True:
            self.running()


t_light = TrafficLight()
print(t_light.running())
