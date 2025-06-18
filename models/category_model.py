from storage import get_connection, close_connection


def get_category_by_id(id_category):
    conn, cursor = get_connection()
    query = "SELECT * FROM categories WHERE id_category = %s"
    cursor.execute(query, (id_category,))
    category = cursor.fetchone()
    close_connection(conn, cursor)
    return category


def get_all_categories():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM categories WHERE id_category != 1")
    categories = cursor.fetchall()
    close_connection(conn, cursor)
    return categories


def update_categories(new_name, id_category):
    conn, cursor = get_connection()
    upd_query = "UPDATE categories SET category_name = %s WHERE id_category = %s"
    cursor.execute(upd_query, (new_name, id_category))
    conn.commit()
    close_connection(conn, cursor)


def insert_to_categories(category_name):
    conn, cursor = get_connection()
    insert_query = "INSERT INTO categories (category_name) VALUES (%s)"
    cursor.execute(insert_query, (category_name,))
    conn.commit()
    close_connection(conn, cursor)
