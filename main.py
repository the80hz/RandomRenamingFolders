import os
import shutil
from random_all import random_int


if __name__ == '__main__':
    pathname = input('Введите путь: ')
    n = 999

    # проходимся по всем папкам в директории
    for entry in os.listdir(pathname):
        if os.path.isdir(os.path.join(pathname, entry)):
            value = random_int(1, n)

            # проверяем, не занято ли число
            for folder in os.listdir(pathname):
                while folder == value:
                    value = random_int(1, n)

            # переименование
            shutil.move(pathname + '/' + entry, pathname + '/' + value)
