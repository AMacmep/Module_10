# Домашнее задание по теме "Создание потоков".
import time
import threading
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    work_file = open(file_name, 'w', encoding='utf-8')
    for word_number in range(word_count):
        work_file.write(f'Какое-то слово №{word_number + 1}\n')
        time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_finish = datetime.now()
fime_work_function = time_finish - time_start
print(f'Работа последоваетльно {fime_work_function} c')

time_start = datetime.now()
thr_one = Thread(target=write_words, args=(10, 'example5.txt'))
thr_two = Thread(target=write_words, args=(30, 'example6.txt'))
thr_three = Thread(target=write_words, args=(200, 'example7.txt'))
thr_four = Thread(target=write_words, args=(100, 'example8.txt'))

thr_one.start()
thr_two.start()
thr_three.start()
thr_four.start()

thr_one.join()
thr_two.join()
thr_three.join()
thr_four.join()

time_finish = datetime.now()
fime_work_function = time_finish - time_start
print(f'Работа потоков {fime_work_function} с')
