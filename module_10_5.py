# Домашнее задание по теме "Многопроцессное программирование"
# Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.
from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    file_n = open(name, 'r', encoding='utf-8')
    while True:
        file_line = (file_n.readline().replace('\n', ''))
        if not file_line:
            break
        all_data.append(file_line)

if __name__ == '__main__':
    list_files = ('file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt')
    start_time_1 = datetime.now()
    for name_file in list_files:
        full_name_file = './text/' + name_file
        read_info(full_name_file)
    time_read_info = datetime.now() - start_time_1
    print(f'{time_read_info} (линейный)')


    start_time = datetime.now()
    with multiprocessing.Pool(4) as pool:
        name_file_m = []
        for number_file in range(1, 5):
            name_file_m.append(f'./text/file {number_file}.txt')
        pool.map(read_info, name_file_m)
    time_multiprocessing = datetime.now() - start_time
    print(f'{time_multiprocessing} (многопроцессный)')
