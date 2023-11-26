# -*- coding: cp1251 -*-
import random
import logging
from datetime import datetime
logging.basicConfig(filename='game.log', format='%(asctime)s [%(levelname)s] %(message)s', level=logging.DEBUG)

def a(N, k):
    number = random.randint(1, N)
    logging.info(f"�������� ����� �� 1 �� {N}")
    logging.info(f"� ��� {k} �������")
    popitki = 0
    while popitki < k:
        try:
            u_number = int(input("�������� �����: "))
            logging.info(f"������� ������������: {u_number}")
        except ValueError:
            print("�� ����� ������������ ��������. ���������� ��� ���.")
            logging.error("������������ ���� ������������ ��������.")
            continue

        if u_number == number:
            logging.info("������������ ������ �����.")
            print("����������! �� ������� �����!")
            return

        if u_number < number:
            logging.info("������������ ���� ����� ������ �����������.")
            print("���������� ����� ������")
        else:
            logging.info("������������ ���� ����� ������ �����������.")
            print("���������� ����� ������")

        popitki += 1

    logging.info("������� �����������.")
    print("������� �����������. �� �� ������� �����.")


if __name__ == "__main__":
    try:
        N = int(input("������� ������� ��� ������������� �����: "))
        logging.info(f"������� ������� ��� ������������� �����: {N}")
        k = int(input("������� ���������� �������: "))
        logging.info(f"���������� �������: {k}")
        a(N, k)
    except ValueError:
        print("�� ����� ������������ ��������. ���������� ��� ���.")
        logging.error("������������ ���� ������������ ��������.")