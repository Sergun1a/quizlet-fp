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
    """
    dictionary['dictionary'][purify(word)] = purify(translation)

    return dictionary
