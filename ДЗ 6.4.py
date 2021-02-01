class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self):
        direction = input('Введите "r" для поворота направо, или "l" для поворота налево. Иначе машина едет прямо')
        if direction == 'r':
            print('Поворачиваем направо')
        elif direction == 'l':
            print('Поворачиваем налево')
        else:
            print('Прдолжаем ехать прямо!')

    def show_speed(self):
        print(f'Скорость данного автомобиля {self.speed} километров в час')
        return self.speed

class TownCar(Car):

    pass

class SportCar(Car):
    pass

class WorkCar(Car):
    pass

class PoliceCar(Car):
    pass

tcar = TownCar(65,'blue', 'honda', False)
b = tcar.show_speed()
print('Обнаружено превышение скорости') if b > 60 else None

wcar = WorkCar(35,'blue', 'honda', False)
v = wcar.show_speed()
print('Обнаружено превышение скорости') if v > 40 else None