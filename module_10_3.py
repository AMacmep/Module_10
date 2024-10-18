# Домашнее задание по теме "Блокировки и обработка ошибок"
# Задача "Банковские операции":

import threading
from random import randint
from threading import Lock, Thread
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            replenishment = randint(50, 500)
            self.balance += replenishment
            print(f"Пополнение: {replenishment}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(100):
            withdrawal = randint(50, 500)
            print(f'Запрос на {withdrawal}')
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f'Снятие: {withdrawal}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
