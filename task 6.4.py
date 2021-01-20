# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
#  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула(куда).
#  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#  Для классов TownCar и WorkCar переопределите метод show_speed.
#  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

        # methods
    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'текущая скорость {self.name} : {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(
            f'текущая скорость городского автомобиля {self.name} : {self.speed} км/ч')

        if self.speed > 40:
            return f'скорость {self.name} выше разрешенной'
        else:
            return f'скорость {self.name} разрешенная'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(
            f'текущая скорость рабочего атомобиля{self.name} : {self.speed} км/ч')

        if self.speed > 60:
            return f'скорость{self.name} выше разрешенной'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции'
        else:
            return f'{self.name} не из полиции'


bmw = SportCar(100, 'black', 'BMW', False)
ford = TownCar(30, 'orange', 'Ford', False)
audi = WorkCar(70, 'green', 'Audi', True)
lada = PoliceCar(110, 'Blue', 'Lada', True)
print(lada.turn_left())
print(f'когда {ford.turn_right()}, тогда {audi.stop()}')
print(f'{lada.go()} со скоростью {lada.show_speed()}')
print(f'{lada.name} цвета {lada.color}')
print(f' {lada.name}  полицейский автомобиль? {lada.is_police}')
print(audi.show_speed())
print(ford.show_speed())
print(ford.police())
print(ford.show_speed())
