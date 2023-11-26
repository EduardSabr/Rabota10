# ниже под следующей решеткой, строчка. Это скорее у меня файл в кодировке cp1251, если же убрать это, но код работает не будет, выдаст ошибку (UTF-8)
# -*- coding: cp1251 -*-
import random
import logging
from datetime import datetime
# настройка логгера
logging.basicConfig(filename='game.log', format='%(asctime)s [%(levelname)s] %(message)s', level=logging.DEBUG)

def a(N, k):
    number = random.randint(1, N)
    logging.info(f"Загадано число от 1 до {N}")
    logging.info(f"У вас {k} попыток")
    popitki = 0
    while popitki < k:
        try:
            u_number = int(input("Угадайте число: "))
            logging.info(f"Попытка пользователя: {u_number}")
        except ValueError:
            print("Вы ввели некорректное значение. Попробуйте еще раз.")
            logging.error("Пользователь ввел некорректное значение.")
            continue

        if u_number == number:
            logging.info("Пользователь угадал число.")
            print("Поздравляю! Вы угадали число!")
            return

        if u_number < number:
            logging.info("Пользователь ввел число меньше загаданного.")
            print("Загаданное число больше")
        else:
            logging.info("Пользователь ввел число больше загаданного.")
            print("Загаданное число меньше")

        popitki += 1

    logging.info("Попытки закончились.")
    print("Попытки закончились. Вы не угадали число.")


if __name__ == "__main__":
    try:
        N = int(input("Введите границу для загадываемого числа: "))
        logging.info(f"Верхняя граница для загадываемого числа: {N}")
        k = int(input("Введите количество попыток: "))
        logging.info(f"Количество попыток: {k}")
        a(N, k)
    except ValueError:
        print("Вы ввели некорректное значение. Попробуйте еще раз.")
        logging.error("Пользователь ввел некорректное значение.")
