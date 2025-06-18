from services.categories import get_dict_categories
from utils.formatting import format_date
from models.statistic_model import (
    get_month_expense,
    get_month_income,
    fetch_unique_months,
    fetch_statistics,
)
from config import MONTH_DEFAULT


def get_dict_unique_months():
    unique_months = fetch_unique_months()
    month_dict = {}
    for i, uni in enumerate(unique_months, start=1):
        month_dict[i] = uni["date"]
    return month_dict


def show_statistics(month=MONTH_DEFAULT):

    print(f"\nСводка расходов за {format_date(month)}:\n")
    statistic = fetch_statistics(month)
    category_dict = get_dict_categories()
    month_expense = get_month_expense(month)
    month_income = get_month_income(month)

    for stat in statistic:
        category_name = category_dict.get(stat["id_category"], "Неизвестно")
        print(f"{category_name} - {stat['amount']}")

    print(f"\nРасходы за месяц - {month_expense}")
    print(f"Доходы за месяц - {month_income}")
