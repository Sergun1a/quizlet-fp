from helpers.helpers import wait, clear_screen, purify


class Menu:
    def main_menu(self):
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

    def translatation_type_select(self, dictionaries):
        """
        Выбираю тип перевода. С русского на английский или наоборот с английского на русский

        :param dictionaries: доступные для добавления переводов словари
        :return: none
        """
        clear_screen()
        print("1. " + dictionaries[0].primary_language + " на " + dictionaries[0].secondary_language)
        print("2. " + dictionaries[1].primary_language + " на " + dictionaries[1].secondary_language)
        chosen_type = wait(("1", "2"))
        self.translation_start(dictionaries[int(chosen_type) - 1])

    def translation_start(self, dictionary):
        """
        Начинаю перевод. Запрашиваю данные у пользователя и добавляю их в словарь.

        :param dictionary: словарь в который будут добавляться переводы
        :return: none
        """
        clear_screen()
        translation_data = dictionary.request_translation_data()
        dictionary.add_new_translation(translation_data[0], translation_data[1])
        chosen_action = dictionary.post_addition_actions()
        if chosen_action == purify("N"):
            self.translation_start(dictionary)

    def quizlet_start(self, quizlet):
        """
        Начинаю викторину. Выбираю случайное слово из случайного словаря и отображаю его пользователю для перевода.

        :param quizlet:
        :return: none
        """
        clear_screen()
        res = quizlet.random_translation()
        if res:
            quizlet.results("Вы перевели все слова во всех словарях.\n")
            wait('S')
        else:
            quizlet.post_translation_actions()
            chosen_action = wait(('N', 'S', 'R'))
            if chosen_action == purify('N'):
                self.quizlet_start(quizlet)
            if chosen_action == purify('R'):
                quizlet.results()
                wait('S')

    def help(self):
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
