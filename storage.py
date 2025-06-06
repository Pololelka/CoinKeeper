import mysql.connector


def get_connection():
    conn = mysql.connector.connect(
        user="root", password="12345678", host="127.0.0.1", database="coinkeeper"
    )
    cursor = conn.cursor(dictionary=True)
    return conn, cursor


def close_connection(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


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
