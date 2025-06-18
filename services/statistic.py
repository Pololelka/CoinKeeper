import datetime
from services.categories import get_all_categories, get_dict_categories
from storage import get_connection, close_connection
from utils.formatting import format_date

month_default = datetime.date.today().isoformat()[:-3]


def get_unique_months():
    conn, cursor = get_connection()

    query = "SELECT DISTINCT DATE_FORMAT(date, '%Y-%m') AS date FROM transactions ORDER BY date DESC"
    cursor.execute(query)
    unique_months = cursor.fetchall()

    close_connection(conn, cursor)

    month_dict = {}
    for i, uni in enumerate(unique_months, start=1):
        month_dict[i] = uni["date"]
    return month_dict


def get_month_income(month):
    conn, cursor = get_connection()

    query = "SELECT SUM(amount) as sum FROM transactions WHERE id_category = 1 AND date LIKE %s"
    cursor.execute(query, (f"{month}%",))
    month_income = cursor.fetchone()

    close_connection(conn, cursor)

    if month_income and month_income["sum"] is not None:
        return int(month_income["sum"])
    else:
        return 0


def get_month_amount(month):
    conn, cursor = get_connection()

    query = "SELECT SUM(amount) as sum FROM transactions WHERE date LIKE %s AND id_category != 1"

    cursor.execute(query, (f"{month}%",))
    month_amount = cursor.fetchone()

    close_connection(conn, cursor)

    if month_amount and month_amount["sum"] is not None:
        return int(month_amount["sum"])
    else:
        return 0


def fetch_statistics(month=month_default):
    conn, cursor = get_connection()

    query = "SELECT id_category, SUM(amount) as amount FROM transactions WHERE date LIKE %s AND id_category != 1 GROUP BY id_category"
    cursor.execute(query, (f"{month}%",))
    statistic = cursor.fetchall()

    close_connection(conn, cursor)
    return statistic


def show_statistics(month=month_default):

    print(f"\nСводка расходов за {format_date(month)}:\n")
    statistic = fetch_statistics(month)
    category_dict = get_dict_categories()
    month_amount = get_month_amount(month)
    month_income = get_month_income(month)

    for stat in statistic:
        category_name = category_dict.get(stat["id_category"], "Неизвестно")
        print(f"{category_name} - {stat['amount']}")

    print(f"\nРасходы за месяц - {month_amount}")
    print(f"Доходы за месяц - {month_income}")
