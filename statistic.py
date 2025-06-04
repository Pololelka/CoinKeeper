import datetime
from storage import load_file, format_date


month_default = datetime.date.today().isoformat()[:-3]

FILE_CATEGORIES = "data/categories.json"
FILE_HISTORY = "data/history.json"


def show_statistics(month=month_default):
    history = load_file(FILE_HISTORY)
    categories = load_file(FILE_CATEGORIES)

    print(f"\nСводка расходов за {format_date(month)}:\n")

    mohth_amount = 0
    month_income = 0
    for cat in categories:
        if cat["id"] == 0:
            continue
        category_amount = 0
        for his in history:
            if cat["id"] == his["id_category"] and his["date"][:-3] == month:
                category_amount += his["amount"]
        mohth_amount += category_amount
        print(f"{cat["category_name"]} - {category_amount}")

    for his in history:
        if his["id_category"] == 0 and his["date"][:-3] == month:
            month_income += his["amount"]

    print(f"\nРасходы за месяц - {mohth_amount}")
    print(f"Доходы за месяц - {month_income}")


def get_unique_months():
    history = load_file(FILE_HISTORY)
    unique_month = set()

    for his in history:
        unique_month.add(his["date"][:-3])

    unique_month = list(unique_month)
    unique_month.sort(reverse=True)

    month_dict = {}
    for i, uni in enumerate(unique_month, start=1):
        month_dict[i] = uni
    return month_dict


def statistic_menu():
    show_statistics()
    while True:
        unique_month = get_unique_months()
        print("\nПоказать статистику за:")
        for i in unique_month:
            print(f"{i}. {format_date(unique_month[i])}")
        print("0. Выйти")

        choice = int(input("\nВыберите действие: "))

        if choice == 0:
            print("Назад")
            break
        elif choice in unique_month:
            show_statistics(unique_month[choice])
        else:
            print("Неверный выбор. Попробуйте снова.")
