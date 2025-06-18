from storage import get_connection, close_connection


def get_balance():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM balance")
    balance = cursor.fetchone()
    close_connection(conn, cursor)
    return balance["balance"]


def update_balance(balance):
    conn, cursor = get_connection()
    upd_query = "UPDATE balance SET balance = %s WHERE id_balance = 1"
    cursor.execute(upd_query, (balance,))
    conn.commit()
    close_connection(conn, cursor)
