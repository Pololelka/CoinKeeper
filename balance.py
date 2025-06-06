from storage import get_connection, close_connection


def add_to_balance(id_catogory, amount):
    balance = get_balance()
    balance += -amount if id_catogory != 1 else amount
    update_balance(balance)


def delete_from_balance(id_catogory, amount):
    balance = get_balance()
    balance += amount if id_catogory != 1 else -amount
    update_balance(balance)


def get_balance():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM balance")
    balance = cursor.fetchall()
    close_connection(conn, cursor)
    return balance[0]["balance"]


def update_balance(balance):
    conn, cursor = get_connection()
    upd_query = "UPDATE balance SET balance = %s WHERE id_balance = 1"
    cursor.execute(upd_query, (balance,))
    conn.commit()
    close_connection(conn, cursor)
