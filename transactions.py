import datetime
from storage import get_connection, close_connection
from categories import show_categories, found_category, get_dict_categories
from balance import add_to_balance, delete_from_balance


def show_history():

    # if not history:
    #     print("Пока нет операций.")
    #     return

    print("История операций:\n")

    category_dict = get_dict_categories()
    history = get_all_history()

    for transaction in history:
        id_category = transaction["id_category"]
        category_name = category_dict.get(id_category, "Неизвестно")
        print(
            f"{transaction['id_transaction']}. "
            f"Сумма: {transaction['amount']}, "
            f"Категория: {category_name}, "
            f"Заметки: {transaction['note']}, "
            f"Дата: {transaction['date']}"
        )


def add_transaction(operation="-"):

    # if not categories and operation != "+":
    #     print("Действие недоступно. Пока нет категорий.")
    #     return
    try:
        amount = int(input("Введите сумму операции: "))
    except ValueError:
        print("Ошибка: введите число.")
        return

    if operation != "+":
        show_categories()
        id_category = found_category()
    else:
        id_category = 1

    add_to_balance(id_category, amount)

    note = input("Введите комментарий (необязательно): ")

    date = datetime.date.today().isoformat()

    insert_to_history(amount, id_category, note, date)

    print("Операция добавлена!")


def found_transaction():
    history = get_all_history()
    while True:
        try:
            id_transaction = int(input("Введите ID операции: "))
        except ValueError:
            print("Ошибка: введите число.")
            continue

        if any(item.get("id_transaction") == id_transaction for item in history):
            return id_transaction
        else:
            print("Такой операции не существует, попробуйте еще раз.")


def edit_transaction():
    # if not history:
    #     print("Действие недоступно. Пока нет операций.")
    #     return

    print("Изменение операции")
    id_transaction = found_transaction()
    show_categories()

    id_category = int(input("Введите новую категорию для операции: "))
    amount = int(input("Введите новую сумму для операции: "))

    old_transaction = get_transaction_by_id(id_transaction)

    update_history(amount, id_category, id_transaction)

    delete_from_balance(old_transaction[0]["id_category"], old_transaction[0]["amount"])
    add_to_balance(id_category, amount)
    category_dict = get_dict_categories()

    category_name = category_dict.get(id_category, "Неизвестно")

    print(f"Операция успешно изменена на {amount} в категории '{category_name}'.")


def delete_transaction():

    # if not history:
    #     print("Действие недоступно. Пока нет операций.")
    #     return

    id_transaction = found_transaction()
    old_transaction = get_transaction_by_id(id_transaction)

    delete_from_history(id_transaction)
    delete_from_balance(old_transaction[0]["id_category"], old_transaction[0]["amount"])
    print(f"Операция с ID {id_transaction} успешно удалена.")

    # print(f"Операция с ID {id_transaction} не найдена.")


def get_all_history():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM history")
    history = cursor.fetchall()
    close_connection(conn, cursor)
    return history


def get_transaction_by_id(id_transaction):
    conn, cursor = get_connection()
    query = "SELECT * FROM history WHERE id_transaction = %s"
    cursor.execute(query, (id_transaction,))
    history_by_id = cursor.fetchall()
    close_connection(conn, cursor)
    return history_by_id


def update_history(amount, id_category, id_transaction):
    conn, cursor = get_connection()
    upd_query = (
        "UPDATE history SET amount = %s, id_category = %s WHERE id_transaction = %s"
    )
    cursor.execute(upd_query, (amount, id_category, id_transaction))
    conn.commit()
    close_connection(conn, cursor)


def insert_to_history(amount, id_category, note, date):
    conn, cursor = get_connection()
    inser_query = (
        "INSERT INTO history (amount, id_category, note, date) VALUES (%s,%s,%s,%s)"
    )
    cursor.execute(inser_query, (amount, id_category, note, date))
    conn.commit()
    close_connection(conn, cursor)


def delete_from_history(id_transaction):
    conn, cursor = get_connection()
    del_query = "DELETE FROM history WHERE id_transaction = %s"
    cursor.execute(del_query, (id_transaction,))
    conn.commit()
    close_connection(conn, cursor)


def history_menu():
    show_history()
    while True:
        print("\n1. Добавить расход")
        print("2. Добавить доход")
        print("3. Редактировать операцию")
        print("4. Удалить операцию")
        print("0. Назад")

        choice = input("\nВыберите действие: ")

        if choice == "1":
            add_transaction("-")
        elif choice == "2":
            add_transaction("+")
        elif choice == "3":
            edit_transaction()
        elif choice == "4":
            delete_transaction()
        elif choice == "0":
            print("Назад")
            break
