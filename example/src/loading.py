# -*- coding: UTF-8 -*-

from itertools import cycle
from time import sleep


def load():
    clock = cycle(['🕛', '🕑', '🕓', '🕕', '🕗', '🕘', '🕚'])
    msg = 'Loading... '
    for i in range(10):
        print('\r' + msg + next(clock), end='')
        sleep(1)

    print('\n Successfull 👍')


if __name__ == '__main__':
    load()
