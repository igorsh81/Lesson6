# Реализовать базовый класс Worker (работник).
# Определить атрибуты: name, surname, position (должность), income (доход);
# Последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# Создать класс Position (должность) на базе класса Worker;
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# Проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name='Михаил', surname='Потапов', position='Вышибала', wage=100, bonus=20):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'оклад': wage, 'премия': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f" {self.name} {self.surname} {self._income}")

    def get_total_income(self):
        print(f" Доход с учетом премии {sum(self._income.values())} руб. на позиции {self.position}")


miha = Position("Михаил", "Потапов", "Вышибала", 33200, 10000)
miha.get_full_name()
miha.get_total_income()
