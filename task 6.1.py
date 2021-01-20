# 1. Создать класс TrafficLight(светофор) и определить у него один атрибут color(цвет) и метод running(запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния(красный) составляет 7 секунд, второго(желтый) — 2 секунды,
# третьего(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.

from time import sleep
from datetime import datetime as dt


class TrafficLight:

    _mode = {'red': 7, 'yellow': 2, 'green': 7}
    _color = ''

    def running(self):

        for color, m_time in self._mode.items():
            self._color = color
            start_mode_time = dt.now()

            print(f"TrafficLight перешел в состояние '{self._color}' "
                  f"on {m_time} seconds")

            sleep(m_time)

            print(f"TrafficLight закончилась работа цвета '{self._color}' after"
                  f"{(dt.now() - start_mode_time).seconds} seconds")


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
