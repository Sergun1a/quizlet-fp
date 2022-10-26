from classes.menu.menu import *
from classes.quizlet.quizlet import *
from classes.dictionary.default_dictionary import *

# инициирую словари
dictionaries = [init_dictionary({"один": "one", "два": "two"}, "Русский", "Английский"),
                init_dictionary({"one": "один", "two": "два"}, "Английский", "Русский")]

while 1:
    menu_action = main_menu()
    if menu_action == "1":
        dictionaries = translatation_type_select([dictionaries[0], dictionaries[1]])
    if menu_action == "2":
        quizlet = init_quizlet([dictionaries[0], dictionaries[1]])
        quizlet_start(quizlet)
    if menu_action == "3":
        help()
