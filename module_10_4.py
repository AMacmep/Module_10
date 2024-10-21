# Домашнее задание по теме "Очереди для обмена данными между потоками."
# Цель: Применить очереди в работе с потоками, используя класс Queue.
from threading import Thread
from random import randint
from time import sleep
from queue import Queue


class Table():
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe():
    list_thr = []

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest == None:
                    table.guest = guest.name
                    guest.start()
                    print(f'{table.guest} сел(-а) за стол номер {table.number}')
                    break
            if not guest.is_alive():
                cafe.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        table_is_busy = True
        while not cafe.queue.empty() or table_is_busy:
            for table in self.tables:
                guest_name = table.guest
                for guest in guests:
                    if guest_name == guest.name:
                        if not guest.is_alive():
                            print(f'{guest.name} покушал(-а) и ушёл(ушла)')
                            print(f'Стол номер {table.number} свободен')
                            table.guest = None
                            guest.join()
                            if not cafe.queue.empty():
                                guest = cafe.queue.get()
                                print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                                table.guest = guest.name
                                guest.start()
                        break
            table_is_busy = False
            for table in self.tables:
                if not table.guest is None:
                    table_is_busy = True
                    break

    def check_table(self):
        for table in self.tables:
            if table.guest is not None:
                return True
        return False


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
