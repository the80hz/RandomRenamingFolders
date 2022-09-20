import os
from random import randint


if __name__ == '__main__':
    # pathname = input('Введите путь: ')
    # pathname = '/Users/the80hz/Yandex.Disk.localized/poggers'
    pathname = '/Users/the80hz/Downloads/'
    for entry in os.listdir(pathname):
        if os.path.isdir(os.path.join(pathname, entry)):
            value = str(randint(1, 20))
            os.rename(pathname + '/' + entry, pathname + '/' + value)
