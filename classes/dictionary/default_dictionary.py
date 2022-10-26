from helpers.helpers import wait, purify


def init_dictionary(dictionary, primary_language, secondary_language):
    res = dict()
    res['dictionary'] = dictionary
    res['primary_language'] = primary_language
    res['secondary_language'] = secondary_language
    return res


def add_new_translation(dictionary, word, translation):
    """
    Добавляю в словарь новый перевод

    :param dictionary: Словарь
    :param word: слово на базовом языке
    :param translation: переведенное слово
    :return: none
    """
    user_input = purify('Y')
    if purify(word) in dictionary['dictionary']:
        print("Перевод слова \"{}\" уже есть в словаре. Желаете обновить перевод?\tY|N\n".format(word))
        user_input = wait(('Y', 'N'))

    if user_input == purify('Y'):
        dictionary['dictionary'][purify(word)] = purify(translation)
        print("Перевод слова \"{}\" был добавлен.\n".format(word))

    return dictionary


def post_addition_actions():
    """
    Вывожу сообщение с вариантами действия после добавления перевода

    :return:
    """
    print("Нажмите клавишу N, если хотите добавить ещё один перевод или клавишу S для выхода в меню программы.\tN|S\n")
    return wait(('N', 'S'))


def request_translation_data(dictionary):
    """
    Запрашиваю у пользователя данные о переводе слова

    :return: кортеж вида ("слово на базовом языке", "его перевод")
    """
    print("Базовый язык: {}. Перевод на {}\n".format(dictionary['primary_language'], dictionary['secondary_language']))
    primary_word = purify(input("Введите слово на базовом языке\n"))
    translation = purify(input("Введите перевод для \"{0}\"\n".format(primary_word)))
    return primary_word, translation
