from models.balance_model import get_balance
from ui.category_menu import categories_menu
from ui.transaction_menu import history_menu
from ui.statistic_menu import statistic_menu


def print_main_menu():
    print("\nГлавное меню:")
    print(f"\nТекущий баланс - {get_balance()}")
    print("\n1. Показать историю")
    print("2. Показать категории")
    print("3. Сводка")
    print("0. Выйти")


def run_main_menu():
    while True:
        print_main_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            history_menu()
        elif choice == "2":
            categories_menu()
        elif choice == "3":
            statistic_menu()
        elif choice == "0":
            print("👋 Выход.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")
