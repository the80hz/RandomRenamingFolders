import os
from random_all import random_int


if __name__ == '__main__':
    pathname = input('Введите путь: ')

    # проходимся по всем папкам в директории
    for entry in os.listdir(pathname):
        if os.path.isdir(os.path.join(pathname, entry)):
            value = random_int(1, 20)

            # проверяем, не занято ли число
            for folder in os.listdir(pathname):
                while folder == value:
                    value = random_int(1, 20)

            # переименование
            os.rename(pathname + '/' + entry, pathname + '/' + value)
