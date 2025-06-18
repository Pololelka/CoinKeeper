from db.connection import get_connection, close_connection
from config import INCOME_CATEGORY_ID, MONTH_DEFAULT


def get_month_expense(month):
    conn, cursor = get_connection()
    query = "SELECT SUM(amount) as sum FROM transactions WHERE date LIKE %s AND id_category != %s"
    cursor.execute(query, (f"{month}%", INCOME_CATEGORY_ID))
    month_expense = cursor.fetchone()
    close_connection(conn, cursor)
    if month_expense and month_expense["sum"] is not None:
        return int(month_expense["sum"])
    else:
        return 0


def get_month_income(month):
    conn, cursor = get_connection()
    query = "SELECT SUM(amount) as sum FROM transactions WHERE date LIKE %s AND id_category = %s"
    cursor.execute(query, (f"{month}%", INCOME_CATEGORY_ID))
    month_income = cursor.fetchone()
    close_connection(conn, cursor)
    if month_income and month_income["sum"] is not None:
        return int(month_income["sum"])
    else:
        return 0


def fetch_unique_months():
    conn, cursor = get_connection()
    query = "SELECT DISTINCT DATE_FORMAT(date, '%Y-%m') AS date FROM transactions ORDER BY date DESC"
    cursor.execute(query)
    unique_months = cursor.fetchall()
    close_connection(conn, cursor)
    return unique_months


def fetch_statistics(month=MONTH_DEFAULT):
    conn, cursor = get_connection()
    query = "SELECT id_category, SUM(amount) as amount FROM transactions WHERE date LIKE %s AND id_category != %s GROUP BY id_category"
    cursor.execute(query, (f"{month}%", INCOME_CATEGORY_ID))
    statistic = cursor.fetchall()
    close_connection(conn, cursor)
    return statistic
