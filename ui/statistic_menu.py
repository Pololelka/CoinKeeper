from services.statistic_service import (
    show_statistics,
    get_dict_unique_months,
    format_date,
)
from utils.input_helpers import input_choise_menu


def statistic_menu():
    show_statistics()
    while True:
        unique_month = get_dict_unique_months()
        print("\nПоказать статистику за:")
        for i in unique_month:
            print(f"{i}. {format_date(unique_month[i])}")
        print("0. Выйти")

        choice = input_choise_menu()

        if choice == 0:
            print("Назад")
            break
        elif choice in unique_month:
            show_statistics(unique_month[choice])
        else:
            print("Неверный ввод. Попробуйте снова.")
