from classes.dictionary.default_dictionary import DefaultDictionary
from classes.menu.menu import Menu
from classes.quizlet.quizlet import Quizlet

# инициирую импортированные классы
ru_en_dict = DefaultDictionary({"один": "one", "два": "two"}, "Русский", "Английский")
en_ru_dict = DefaultDictionary({"one": "один", "two": "два"}, "Английский", "Русский")
menu = Menu()

while 1:
    menu_action = menu.main_menu()
    if menu_action == "1":
        menu.translatation_type_select((ru_en_dict, en_ru_dict))
    if menu_action == "2":
        quizlet = Quizlet((ru_en_dict, en_ru_dict))
        menu.quizlet_start(quizlet)
    if menu_action == "3":
        menu.help()
