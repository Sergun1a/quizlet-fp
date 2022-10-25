import random

from helpers.helpers import clear_screen, purify


class Quizlet:
    __ru_en_correct_translations = 0
    __ru_en_total_translations = 0
    __en_ru_correct_translations = 0
    __en_ru_total_translations = 0

    __ru_en_translations = {}
    __en_ru_translations = {}

    def __init__(self, dictionaries):
        self.__ru_en_dict = dictionaries[0]
        self.__en_ru_dict = dictionaries[1]
        self.__ru_en_translations = dictionaries[0].get_dictionary
        self.__en_ru_translations = dictionaries[1].get_dictionary

    @property
    def ru_translations(self):
        return self.__ru_en_translations

    @property
    def en_translations(self):
        return self.__en_ru_translations

    def random_translation(self):
        """
        Запрашиваю перевод случайного слова из выбранного словаря

        :return: str|none
        """
        chosen_dict = random.randint(0, 1)
        lang = ""
        if (len(self.ru_translations) == 0) and (len(self.en_translations) == 0):
            return "out_of_translations"

        if self.ru_translations and self.en_translations:
            if chosen_dict == 0:
                lang = "ru"
                dictionary = self.__ru_en_dict
                translations = self.__ru_en_translations
            else:
                lang = "en"
                dictionary = self.__en_ru_dict
                translations = self.__en_ru_translations

        if self.ru_translations and (len(self.en_translations) == 0):
            lang = "ru"
            dictionary = self.__ru_en_dict
            translations = self.__ru_en_translations

        if (len(self.ru_translations) == 0) and self.en_translations:
            lang = "en"
            dictionary = self.__en_ru_dict
            translations = self.__en_ru_translations

        print("Перевод из языка \"{}\" на \"{}\" язык\n\n".format(
            dictionary.primary_language, dictionary.secondary_language))
        basic_word = random.sample(translations.keys(), 1)[0]
        translation = purify(input(basic_word + "\t=>\t"))
        if lang == "ru":
            self.__ru_en_total_translations = self.__ru_en_total_translations + 1
        if lang == "en":
            self.__en_ru_total_translations = self.__en_ru_total_translations + 1
        if basic_word in translations:
            if translation == translations[basic_word]:
                if lang == "ru":
                    self.__ru_en_correct_translations = self.__ru_en_correct_translations + 1
                if lang == "en":
                    self.__en_ru_correct_translations = self.__en_ru_correct_translations + 1
                print("\nПравильно\n")
                translations.pop(basic_word)
            else:
                print("\nНеверно. Правильный перевод: {}\n".format(translations[basic_word]))

    def post_translation_actions(self):
        """
        Вывожу доступные действия после ответа на вопрос викторины

        :return: none
        """
        print("\nКлавиша \"N\" - продолжить викторину(следующий перевод)\n"
              "Клавиша \"S\" - завершить викторину и выйти в главное меню\n"
              "Клавиша \"R\" - завершить викторину и просмотреть результаты")

    def results(self, reason=""):
        """
        Вывожу результаты викторины

        :param reason: Причина показа результатов. Например: в пуле переводов закончились слова.
        :return: none
        """
        clear_screen()
        print(reason)

        if self.__en_ru_total_translations == 0:  # избегаю деления на ноль
            en_ru_percent = (self.__en_ru_correct_translations / 1) * 100
        else:
            en_ru_percent = (self.__en_ru_correct_translations / self.__en_ru_total_translations) * 100

        if self.__ru_en_total_translations == 0:
            ru_en_percent = (self.__ru_en_correct_translations / 1) * 100
        else:
            ru_en_percent = (self.__ru_en_correct_translations / self.__ru_en_total_translations) * 100

        print("Всего было переведено слов: {}\n".format(
            self.__ru_en_total_translations + self.__en_ru_total_translations))
        print("Всего переводов с Русского на Английский : {}\n".format(
            self.__ru_en_total_translations))
        print("Правильных переводов с Русского на Английский : {} из {} ({:.2f}%)\n".format(
            self.__ru_en_correct_translations, self.__ru_en_total_translations,
            ru_en_percent))
        print("Всего переводов с Английского на Русский : {}\n".format(
            self.__en_ru_total_translations))
        print("Правильных переводов с Английского на Русский : {} из {} ({:.2f}%)\n".format(
            self.__en_ru_correct_translations, self.__en_ru_total_translations,
            en_ru_percent))
        print("\n\nНажмите клавишу \"S\" для выхода в главное меню\n")
