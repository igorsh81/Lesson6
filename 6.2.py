# Реализовать класс Road (дорога).
# Определить атрибуты: length (длина), width (ширина);
# Значения атрибутов должны передаваться при создании экземпляра класса;атрибуты сделать защищёнными;
# Определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# Проверить работу метода.

class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        leng = self._length
        wid = self._width
        w = self.weight
        dep = self.depth
        total = leng * wid * w * dep / 1000
        return print(f"Масса асфальта\n {leng} м * {wid} м * {w} кг * {dep} см = ", total, "т")


r = Road(20, 5000, 25, 5)
r.mass()
