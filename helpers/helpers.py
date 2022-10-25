import os


def wait(expected_input):
    """
    Ожидание корректного ответа на вопрос от пользователя

    :param expected_input: кортеж ожидаемых символов.
    :return: один из вариантов ожидаемого ввода от пользователя
    """
    user_answer = purify(input())
    while user_answer not in map(purify, expected_input):
        print("Некорректный ввод. Ожидаемые ответы: " + str(expected_input))
        user_answer = purify(input())
    return user_answer


def purify(dirty_string):
    """
    Очищаю строку от мусора и привожу её к нижнему регистру

    :param dirty_string: строка, которую нужно очистить
    :return: очищенную строку (пробелы по краям, символ перевода строки/табуляции/т.д. по краям строки) в нижнем регистре
    """
    return dirty_string.strip().lower()


def clear_screen():
    """
    Очищаю вывод в консоли

    :return: none
    """
    os.system('cls')
