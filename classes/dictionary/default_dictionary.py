from helpers.helpers import wait, purify


class DefaultDictionary:
    __dictionary = {}
    __primary_language = "default_1"
    __secondary_language = "default_2"

    # базовые шаблоны
    __translation_exists = "Перевод слова \"{}\" уже есть в словаре. Желаете обновить перевод?\tY|N\n"
    __successfully_added_translation = "Перевод слова \"{}\" был добавлен.\n"
    __actions_after_adding = "Нажмите клавишу N, если хотите добавить ещё один перевод или клавишу S для выхода в меню программы.\tN|S\n"

    def __init__(self, dictionary, primary_language, secondary_language):
        self.__dictionary = dictionary
        self.__primary_language = primary_language
        self.__secondary_language = secondary_language

    def add_new_translation(self, word, translation):
        """
        Добавляю в словарь новый перевод

        :param word: слово на базовом языке
        :param translation: переведенное слово
        :return: none
        """
        user_input = purify('Y')
        if purify(word) in self.__dictionary:
            print(self.__translation_exists.format(word))
            user_input = wait(('Y', 'N'))

        if user_input == purify('Y'):
            self.__dictionary[purify(word)] = purify(translation)
            print(self.__successfully_added_translation.format(word))

    def post_addition_actions(self):
        """
        Вывожу сообщение с вариантами действия после добавления перевода

        :return:
        """
        print(self.__actions_after_adding)
        return wait(('N', 'S'))

    @property
    def get_dictionary(self):
        """
        Возвращаю копию словаря

        :return: dict
        """
        return self.__dictionary.copy()

    def request_translation_data(self):
        """
        Запрашиваю у пользователя данные о переводе слова

        :return: кортеж вида ("слово на базовом языке", "его перевод")
        """
        print("Базовый язык: {}. Перевод на {}\n".format(self.__primary_language, self.__secondary_language))
        primary_word = purify(input("Введите слово на базовом языке\n"))
        translation = purify(input("Введите перевод для \"{0}\"\n".format(primary_word)))
        return primary_word, translation

    @property
    def primary_language(self):
        return self.__primary_language

    @property
    def secondary_language(self):
        return self.__secondary_language
