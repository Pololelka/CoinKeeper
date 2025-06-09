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
