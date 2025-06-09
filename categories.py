from storage import get_connection, close_connection


def add_category():
    print("\nДобавление новой категории")
    category_name = input("Введите название категории: ").strip()

    if not category_name:
        print("Ошибка: название не может быть пустым.")
        return
    categories = get_all_categories()
    if any(c["category_name"].lower() == category_name.lower() for c in categories):
        print(f"Категория «{category_name}» уже существует.")
        return
    insert_to_categories(category_name)
    print(f"Категория «{category_name}» добавлена!")


def show_categories():
    categories = get_all_categories()
    if not categories:
        print("Пока нет категорий.")
        return

    print("Ваши категории:")
    for category in categories:
        print(f"{category['id_category']}. {category['category_name']}")


def edit_categories():
    categories = get_all_categories()
    if not categories:
        print("Действие недоступно. Пока нет категорий.")
        return
    print("Изменение категории")
    id_category = found_category()
    new_name = input("Введите новое название категории: ").strip()

    old_name = get_category_by_id(id_category)
    update_categories(new_name, id_category)

    print(f"Категория «{old_name[0]['category_name']}» была изменена на «{new_name}».")


def found_category():
    categories = get_all_categories()
    while True:
        try:
            id_category = int(input("Введите ID категории: "))
        except ValueError:
            print("Ошибка: введите число.")
            continue

        if any(item.get("id_category") == id_category for item in categories):
            return id_category
        else:
            print("Такой категории не существует, попробуйте ещё раз.")


def get_dict_categories():
    conn, cursor = get_connection()
    categories = get_all_categories()
    category_dict = {cat["id_category"]: cat["category_name"] for cat in categories}
    close_connection(conn, cursor)
    return category_dict


def get_category_by_id(id_category):
    conn, cursor = get_connection()
    query = "SELECT * FROM categories WHERE id_category = %s"
    cursor.execute(query, (id_category,))
    category = cursor.fetchall()
    close_connection(conn, cursor)
    return category


def update_categories(new_name, id_category):
    conn, cursor = get_connection()
    upd_query = "UPDATE categories SET category_name = %s WHERE id_category = %s"
    cursor.execute(upd_query, (new_name, id_category))
    conn.commit()
    close_connection(conn, cursor)


def get_all_categories():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM categories WHERE id_category != 1")
    categories = cursor.fetchall()
    close_connection(conn, cursor)
    return categories


def insert_to_categories(category_name):
    conn, cursor = get_connection()
    insert_query = "INSERT INTO categories (category_name) VALUES (%s)"
    cursor.execute(insert_query, (category_name,))
    conn.commit()
    close_connection(conn, cursor)


def categories_menu():
    while True:
        show_categories()
        print("\n1. Добавить категорию")
        print("2. Изменить категорию")
        print("0. Назад")

        choice = input("\nВыберите действие: ")

        if choice == "1":
            add_category()
        elif choice == "2":
            edit_categories()
        elif choice == "0":
            print("Назад")
            break
