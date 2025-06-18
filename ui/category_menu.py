from services.categories_service import show_categories, add_category, edit_categories
from utils.input_helpers import input_choise_menu


def categories_menu():
    while True:
        show_categories()
        print("\n1. Добавить категорию")
        print("2. Изменить категорию")
        print("0. Назад")

        choice = input_choise_menu()

        if choice == 1:
            add_category()
        elif choice == 2:
            edit_categories()
        elif choice == 0:
            print("Назад")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")
