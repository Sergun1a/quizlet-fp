from helpers.helpers import wait, clear_screen, purify
from classes.quizlet.quizlet import *
from classes.dictionary.default_dictionary import *


def main_menu():
    """
    Главное меню. Выбор основного действия: добавление перевода, начало викторины, получение справки

    :return:
    """
    clear_screen()
    print("""
        Выберите желаемое действие
        1. Добавить перевод в один из словарей
        2. Начать проверку знаний
        3. Получить справку о работе в программе
        """)
    return wait(("1", "2", "3"))


def translatation_type_select(dictionaries):
    """
    Выбираю тип перевода. С русского на английский или наоборот с английского на русский

    :param dictionaries: доступные для добавления переводов словари
    :return: none
    """
    clear_screen()
    print("1. " + dictionaries[0]['primary_language'] + " на " + dictionaries[0]['secondary_language'])
    print("2. " + dictionaries[1]['primary_language'] + " на " + dictionaries[1]['secondary_language'])
    chosen_type = wait(("1", "2"))
    dictionaries[int(chosen_type) - 1] = translation_start(dictionaries[int(chosen_type) - 1])
    return dictionaries


def translation_start(dictionary):
    """
    Начинаю перевод. Запрашиваю данные у пользователя и добавляю их в словарь.

    :param dictionary: словарь в который будут добавляться переводы
    """
    clear_screen()
    translation_data = request_translation_data(dictionary)

    user_input = purify('Y')
    if purify(translation_data[0]) in dictionary['dictionary']:
        print("Перевод слова \"{}\" уже есть в словаре. Желаете обновить перевод?\tY|N\n".format(translation_data[0]))
        user_input = wait(('Y', 'N'))

    if user_input == purify('Y'):
        dictionary = add_new_translation(dictionary, translation_data[0], translation_data[1])
        print("Перевод слова \"{}\" был добавлен.\n".format(translation_data[0]))

    chosen_action = post_addition_actions()
    if chosen_action == purify("N"):
        translation_start(dictionary)
    return dictionary


def quizlet_start(quizlet):
    """
    Начинаю викторину. Выбираю случайное слово из случайного словаря и отображаю его пользователю для перевода.

    :param quizlet:
    :return: none
    """
    clear_screen()
    basic_word, lang, dictionary, translations = random_translation(quizlet)
    print("Перевод из языка \"{}\" на \"{}\" язык\n\n".format(
        dictionary['primary_language'], dictionary['secondary_language']))
    translation = purify(input(basic_word + "\t=>\t"))
    res = analyze_answer(basic_word, translation, lang, translations, quizlet)
    if res['result']:
        print("\nПравильно\n")
    else:
        print("\nНеверно. Правильный перевод: {}\n".format(translations[basic_word]))

    if (len(quizlet['ru_en_translations']) == 0) and (len(quizlet['en_ru_translations']) == 0):
        quizlet_results = results(quizlet)
        print_results(quizlet, quizlet_results, "Вы перевели все слова во всех словарях.\n")
        wait('S')
    else:
        post_translation_actions()
        chosen_action = wait(('N', 'S', 'R'))
        if chosen_action == purify('N'):
            quizlet_start(res['quizlet'])
        if chosen_action == purify('R'):
            quizlet_res = results(res['quizlet'])
            print_results(quizlet, quizlet_res)
            wait('S')

    return res['quizlet']


def print_results(quizlet, quizlet_res, reason=""):
    print(reason)
    print("Всего было переведено слов: {}\n".format(
        quizlet['ru_en_total_translations'] + quizlet['en_ru_total_translations']))
    print("Всего переводов с Русского на Английский : {}\n".format(
        quizlet['ru_en_total_translations']))
    print("Правильных переводов с Русского на Английский : {} из {} ({:.2f}%)\n".format(
        quizlet['ru_en_correct_translations'], quizlet['ru_en_total_translations'],
        quizlet_res[1]))
    print("Всего переводов с Английского на Русский : {}\n".format(
        quizlet['en_ru_total_translations']))
    print("Правильных переводов с Английского на Русский : {} из {} ({:.2f}%)\n".format(
        quizlet['en_ru_correct_translations'], quizlet['en_ru_total_translations'],
        quizlet_res[0]))
    print("\n\nНажмите клавишу \"S\" для выхода в главное меню\n")


def post_addition_actions():
    """
    Вывожу сообщение с вариантами действия после добавления перевода

    :return:
    """
    print("Нажмите клавишу N, если хотите добавить ещё один перевод или клавишу S для выхода в меню программы.\tN|S\n")
    return wait(('N', 'S'))


def post_translation_actions():
    """
    Вывожу доступные действия после ответа на вопрос викторины

    :return: none
    """
    print("\nКлавиша \"N\" - продолжить викторину(следующий перевод)\n"
          "Клавиша \"S\" - завершить викторину и выйти в главное меню\n"
          "Клавиша \"R\" - завершить викторину и просмотреть результаты")


def request_translation_data(dictionary):
    """
    Запрашиваю у пользователя данные о переводе слова

    :return: кортеж вида ("слово на базовом языке", "его перевод")
    """
    print("Базовый язык: {}. Перевод на {}\n".format(dictionary['primary_language'], dictionary['secondary_language']))
    primary_word = purify(input("Введите слово на базовом языке\n"))
    translation = purify(input("Введите перевод для \"{0}\"\n".format(primary_word)))
    return primary_word, translation


def help():
    """
    Вывожу для пользователя справку о работе с программой

    :return: none
    """
    clear_screen()
    print(""" 
        Справка по работе с программой
        
Вы можете выбрать один из режимов работы:
    1. Добавить новое слово в один из словарей. 
        Для этого введите цифру "1", а затем нажмите клавишу ENTER. 
            После этого вы увидите меню выбора словаря. Нажмите клавишу "1" если желаете добавить перевод с русского на английский, в противном случае введите "2". 
                На следующем шаге приложение попросит вас ввести слово на базовом языке. Введите его и нажмите на клавишу ENTER. После система запросит перевод введенного слова. Введите его и нажмите клавишу ENTER.
                    Вы получите сообщение об успешно добавленном переводе, а также сообщение с дальнейшими вариантами действия: 
                    "N"+ENTER -  если хотите добавить ещё перевод в этом словаре
                    "S"+ENTER - если вы хотите выйти в меню программы.
    2. Начать викторину. 
        Для этого введите цифру "2", а затем нажмите клавишу ENTER.
          В начале перевода вы увидете с какого на какой язык вам нужно перевести слово и также само слово. Введите перевод и нажмите клавишу ENTER.
            После вы увидите корректен ли ваш перевод, а также дальнейшие варианты взаимодействия:
                    "N"+ENTER - получить следующий перевод от программы
                    "S"+ENTER - выйти в главное меню и завершить викторину
                    "R"+ENTER - завершить викторину и увидеть свои результаты
            Стоит отметить, что после корректного перевода слова, оно уберется из пула переводов в текущей викторине.                                    
        """)
    print("\n\nНажмите клавишу \"S\" для выхода в главное меню\n")
    wait('S')
