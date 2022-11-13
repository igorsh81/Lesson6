# Реализуйте базовый класс Car.
# У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police == True:
            print(f'{self.color.title()} {self.name} {self.model} '
                  f'(Police car) is going on a {self.road_type}')
        else:
            print(f'{self.color.title()} {self.name} {self.model} '
                  f'is going on a {self.road_type}')

    def stop(self):
        print('Stopped')

    def turn(self, direction):
        print(f'Turned {direction}')

    def show_speed(self):
        print(f'With speed {self.speed} km/h')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police, model, road_type):
        super().__init__(speed, color, name, is_police)
        self.model = model
        self.road_type = road_type

    def speed_limit(self):
        if self.speed > 60 and self.road_type != 'highway':
            print('Warning! Speed limit violation!')
        elif self.speed > 110:
            print('Warning! Speed limit violation!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police, model, road_type):
        super().__init__(speed, color, name, is_police)
        self.model = model
        self.road_type = road_type

    def speed_limit(self):
        if self.speed > 60 and self.road_type != 'highway':
            print('Warning! Speed limit violation!')
        elif self.speed > 110:
            print('Warning! Speed limit violation!')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, model, road_type):
        super().__init__(speed, color, name, is_police)
        self.model = model
        self.road_type = road_type

    def speed_limit(self):
        if self.speed > 40:
            print('Warning! Speed limit violation!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, model, road_type):
        super().__init__(speed, color, name, is_police)
        self.model = model
        self.road_type = road_type

car1 = TownCar(65, 'red', 'Toyota', False, 'Camry', 'street')
car1.go()
car1.show_speed()
car1.speed_limit()
car1.turn('left')
car1.stop()

print()
car2 = SportCar(100, 'black', 'Ferrari', False, 'F40', 'highway')
car2.go()
car2.show_speed()
car2.speed_limit()
car2.turn('right')
car2.speed = 70
car2.show_speed()
car2.turn('left')
car2.speed = 150
car2.show_speed()
car2.speed_limit()

print()
car3 = WorkCar(45, 'blue', 'Volvo', False, 'FH16', 'street')
car3.go()
car3.show_speed()
car3.speed_limit()
car3.stop()

print()
car4 = PoliceCar(100, 'black', 'Ford', True, 'Police Interceptor', 'street')
car4.go()
car4.show_speed()
car4.stop()
