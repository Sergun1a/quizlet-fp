import random

from helpers.helpers import clear_screen, purify


def init_quizlet(dictionaries):
    quizlet = dict()
    quizlet['ru_en_dict'] = dictionaries[0]
    quizlet['en_ru_dict'] = dictionaries[1]
    quizlet['ru_en_translations'] = dictionaries[0]['dictionary']
    quizlet['en_ru_translations'] = dictionaries[1]['dictionary']
    quizlet['ru_en_total_translations'] = 0
    quizlet['en_ru_total_translations'] = 0
    quizlet['ru_en_correct_translations'] = 0
    quizlet['en_ru_correct_translations'] = 0
    return quizlet


def check_dictionary(quizlet, chosen_dict):
    if quizlet['ru_en_translations'] and quizlet['en_ru_translations']:
        if chosen_dict == 0:
            lang = "ru"
            dictionary = quizlet['ru_en_dict']
            translations = quizlet['ru_en_translations']
        else:
            lang = "en"
            dictionary = quizlet['en_ru_dict']
            translations = quizlet['en_ru_translations']

    if quizlet['ru_en_translations'] and (len(quizlet['en_ru_translations']) == 0):
        lang = "ru"
        dictionary = quizlet['ru_en_dict']
        translations = quizlet['ru_en_translations']

    if (len(quizlet['ru_en_translations']) == 0) and quizlet['en_ru_translations']:
        lang = "en"
        dictionary = quizlet['en_ru_dict']
        translations = quizlet['en_ru_translations']

    return lang, dictionary, translations


def random_translation(quizlet):
    """
    Запрашиваю перевод случайного слова из выбранного словаря

    :return: str|none
    """
    chosen_dict = random.randint(0, 1)
    lang, dictionary, translations = check_dictionary(quizlet, chosen_dict)
    basic_word = random.sample(translations.keys(), 1)[0]
    return basic_word, lang, dictionary, translations


def analyze_answer(basic_word, translation, lang, translations, quizlet):
    res = False
    if lang == "ru":
        quizlet['ru_en_total_translations'] = quizlet['ru_en_total_translations'] + 1
    if lang == "en":
        quizlet['en_ru_total_translations'] = quizlet['en_ru_total_translations'] + 1
    if basic_word in translations:
        if translation == translations[basic_word]:
            if lang == "ru":
                quizlet['ru_en_correct_translations'] = quizlet['ru_en_correct_translations'] + 1
                quizlet['ru_en_translations'].pop(basic_word)
            if lang == "en":
                quizlet['en_ru_correct_translations'] = quizlet['en_ru_correct_translations'] + 1
                quizlet['en_ru_translations'].pop(basic_word)

            res = True
    return {
        "result": res,
        "quizlet": quizlet,
    }


def results(quizlet):
    """
    Подвожу результаты викторины

    :param quizlet: Данные квизлета
    """
    clear_screen()
    if quizlet['en_ru_total_translations'] == 0:  # избегаю деления на ноль
        en_ru_percent = (quizlet['en_ru_correct_translations'] / 1) * 100
    else:
        en_ru_percent = (quizlet['en_ru_correct_translations'] / quizlet['en_ru_total_translations']) * 100

    if quizlet['ru_en_total_translations'] == 0:
        ru_en_percent = (quizlet['ru_en_correct_translations'] / 1) * 100
    else:
        ru_en_percent = (quizlet['ru_en_correct_translations'] / quizlet['ru_en_total_translations']) * 100

    return en_ru_percent, ru_en_percent
