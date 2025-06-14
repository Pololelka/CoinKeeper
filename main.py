from categories import categories_menu
from transactions import history_menu
from statistic import statistic_menu
from storage import load_file
from balance import show_balance

FILE_BALANCE = "data/balance.json"


def print_main_menu():
    print("\nГлавное меню:")
    print(f"\nТекущий баланс - {show_balance()}")
    print("\n1. Показать историю")
    print("2. Показать категории")
    print("3. Сводка")
    print("0. Выйти")


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
