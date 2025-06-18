from db.connection import get_connection, close_connection


def get_all_history():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM transactions")
    history = cursor.fetchall()
    close_connection(conn, cursor)
    return history


def get_transaction_by_id(id_transaction):
    conn, cursor = get_connection()
    query = "SELECT * FROM transactions WHERE id_transaction = %s"
    cursor.execute(query, (id_transaction,))
    history_by_id = cursor.fetchone()
    close_connection(conn, cursor)
    return history_by_id


def update_history(amount, id_category, id_transaction):
    conn, cursor = get_connection()
    upd_query = "UPDATE transactions SET amount = %s, id_category = %s WHERE id_transaction = %s"
    cursor.execute(upd_query, (amount, id_category, id_transaction))
    conn.commit()
    close_connection(conn, cursor)


def insert_to_history(amount, id_category, note, date):
    conn, cursor = get_connection()
    inser_query = "INSERT INTO transactions (amount, id_category, note, date) VALUES (%s,%s,%s,%s)"
    cursor.execute(inser_query, (amount, id_category, note, date))
    conn.commit()
    close_connection(conn, cursor)


def delete_from_history(id_transaction):
    conn, cursor = get_connection()
    del_query = "DELETE FROM transactions WHERE id_transaction = %s"
    cursor.execute(del_query, (id_transaction,))
    conn.commit()
    close_connection(conn, cursor)
