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


def random_translation(quizlet):
    """
    Запрашиваю перевод случайного слова из выбранного словаря

    :return: str|none
    """
    chosen_dict = random.randint(0, 1)
    lang = ""
    if (len(quizlet['ru_en_translations']) == 0) and (len(quizlet['en_ru_translations']) == 0):
        return {
            "result": "out_of_translations",
            "quizlet": quizlet
        }

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

    print("Перевод из языка \"{}\" на \"{}\" язык\n\n".format(
        dictionary['primary_language'], dictionary['secondary_language']))
    basic_word = random.sample(translations.keys(), 1)[0]
    translation = purify(input(basic_word + "\t=>\t"))
    if lang == "ru":
        quizlet['ru_en_total_translations'] = quizlet['ru_en_total_translations'] + 1
    if lang == "en":
        quizlet['en_ru_total_translations'] = quizlet['en_ru_total_translations'] + 1
    if basic_word in translations:
        if translation == translations[basic_word]:
            if lang == "ru":
                quizlet['ru_en_correct_translations'] = quizlet['ru_en_correct_translations'] + 1
            if lang == "en":
                quizlet['en_ru_correct_translations'] = quizlet['en_ru_correct_translations'] + 1
            print("\nПравильно\n")
            translations.pop(basic_word)
        else:
            print("\nНеверно. Правильный перевод: {}\n".format(translations[basic_word]))
    return {
        "result": None,
        "quizlet": quizlet
    }


def post_translation_actions(quizlet):
    """
    Вывожу доступные действия после ответа на вопрос викторины

    :return: none
    """
    print("\nКлавиша \"N\" - продолжить викторину(следующий перевод)\n"
          "Клавиша \"S\" - завершить викторину и выйти в главное меню\n"
          "Клавиша \"R\" - завершить викторину и просмотреть результаты")


def results(quizlet, reason=""):
    """
    Вывожу результаты викторины

    :param quizlet: Данные квизлета
    :param reason: Причина показа результатов. Например: в пуле переводов закончились слова.
    :return: none
    """
    clear_screen()
    print(reason)

    if quizlet['en_ru_total_translations'] == 0:  # избегаю деления на ноль
        en_ru_percent = (quizlet['en_ru_correct_translations'] / 1) * 100
    else:
        en_ru_percent = (quizlet['en_ru_correct_translations'] / quizlet['en_ru_total_translations']) * 100

    if quizlet['ru_en_total_translations'] == 0:
        ru_en_percent = (quizlet['ru_en_correct_translations'] / 1) * 100
    else:
        ru_en_percent = (quizlet['ru_en_correct_translations'] / quizlet['ru_en_total_translations']) * 100

    print("Всего было переведено слов: {}\n".format(
        quizlet['ru_en_total_translations'] + quizlet['en_ru_total_translations']))
    print("Всего переводов с Русского на Английский : {}\n".format(
        quizlet['ru_en_total_translations']))
    print("Правильных переводов с Русского на Английский : {} из {} ({:.2f}%)\n".format(
        quizlet['ru_en_correct_translations'], quizlet['ru_en_total_translations'],
        ru_en_percent))
    print("Всего переводов с Английского на Русский : {}\n".format(
        quizlet['en_ru_total_translations']))
    print("Правильных переводов с Английского на Русский : {} из {} ({:.2f}%)\n".format(
        quizlet['en_ru_correct_translations'], quizlet['en_ru_total_translations'],
        en_ru_percent))
    print("\n\nНажмите клавишу \"S\" для выхода в главное меню\n")
