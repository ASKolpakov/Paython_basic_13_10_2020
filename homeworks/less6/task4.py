"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
import random

class Car:
    is_police = False
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Поехал!')

    def stop(self):
        print('Остановился!')

    def turn(self, direction):
        print(f'Поворачивает на {direction}')

    def show_speed(self):
        print(random.randint(0, 100))




class TownCar(Car):
    def show_speed(self):
        self.speed = random.randint(0, 100)
        print(self.speed)
        if self.speed > 60:
            print('превышаете!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        self.speed = random.randint(0, 100)
        print(self.speed)
        if self.speed > 40:
            print('превышаете!')

class PoliceCar(Car):
    is_police = True



# a = PoliceCar(43, 'blue', 'police')
# a.show_speed()
# print(a.is_police)

# a = WorkCar(43, 'blue', 'bobbi')
# print(a.is_police)
# a.go()
# a.turn('право')
# a.turn('лево')
# a.stop()
# a.show_speed()

# a = WorkCar(43, 'blue', 'bobbi')
# a.show_speed()