# Создать класс TrafficLight (светофор).
# Определить у него один атрибут color (цвет) и метод running (запуск);
# Атрибут реализовать как приватный;
# В рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# Переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()