import mysql.connector
from config import DATABASE


def get_connection():
    conn = mysql.connector.connect(**DATABASE)
    cursor = conn.cursor(dictionary=True)
    return conn, cursor


def close_connection(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()
