import datetime
from categories import get_all_categories
from storage import get_connection, close_connection

month_default = datetime.date.today().isoformat()[:-3]


def format_date(date_str: str) -> str:
    months = {
        "01": "Январь",
        "02": "Февраль",
        "03": "Март",
        "04": "Апрель",
        "05": "Май",
        "06": "Июнь",
        "07": "Июль",
        "08": "Август",
        "09": "Сентябрь",
        "10": "Октябрь",
        "11": "Ноябрь",
        "12": "Декабрь",
    }

    year, month = date_str.split("-")
    return f"{months[month]} {year}"


def get_history_by_mohth(month):
    conn, cursor = get_connection()

    query = "SELECT * FROM history WHERE date LIKE %s"
    cursor.execute(query, (f"{month}%",))
    history_by_mohth = cursor.fetchall()

    close_connection(conn, cursor)
    return history_by_mohth


def get_unique_months():
    conn, cursor = get_connection()

    query = "SELECT DISTINCT DATE_FORMAT(date, '%Y-%m') AS date FROM history ORDER BY date DESC"
    cursor.execute(query)
    unique_months = cursor.fetchall()

    close_connection(conn, cursor)

    month_dict = {}
    for i, uni in enumerate(unique_months, start=1):
        month_dict[i] = uni["date"]
    return month_dict


def get_month_income(month):
    conn, cursor = get_connection()

    query = (
        "SELECT SUM(amount) as sum FROM history WHERE id_category = 1 AND date LIKE %s"
    )
    cursor.execute(query, (f"{month}%",))
    month_income = cursor.fetchone()

    close_connection(conn, cursor)

    if month_income and month_income["sum"] is not None:
        return int(month_income["sum"])
    else:
        return 0


def show_statistics(month=month_default):
    history = get_history_by_mohth(month)
    categories = get_all_categories()

    print(f"\nСводка расходов за {format_date(month)}:\n")

    mohth_amount = 0
    month_income = get_month_income(month)

    for cat in categories:
        category_amount = 0
        for his in history:
            if cat["id_category"] == his["id_category"]:
                category_amount += his["amount"]
        mohth_amount += category_amount
        print(f"{cat["category_name"]} - {category_amount}")

    print(f"\nРасходы за месяц - {mohth_amount}")
    print(f"Доходы за месяц - {month_income}")


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
            print("Неверный ввод. Попробуйте снова.")
