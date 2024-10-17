# Домашнее задание по теме "Потоки на классах"
from threading import Thread
import time

class Knight(Thread):
    day = 0
    left_warriors = 100

    def __init__(self, name:str, power:int):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def battle(self):
        print(f'{self.name}, на нас напали!')

        while left_warriors > 0:
            day += 1
            left_warriors -= self.power
            print(f'{self.name}, сражается {day} дней..., осталось {left_warriors} воинов')
            time.sleep(1)

        print(f'{self.name} одержал победу спустя {day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')