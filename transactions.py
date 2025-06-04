import datetime
from storage import load_file, save_file, format_date
from categories import show_categories, found_category
from balance import add_to_balance, delete_from_balance

FILE_CATEGORIES = "data/categories.json"
FILE_HISTORY = "data/history.json"


def show_history():
    history = load_file(FILE_HISTORY)
    if not history:
        print("Пока нет операций.")
        return

    print("История операций:\n")
    categories = load_file(FILE_CATEGORIES)

    category_dict = {cat["id"]: cat["category_name"] for cat in categories}

    for transaction in history:
        id_category = transaction["id_category"]
        category_name = category_dict.get(id_category, "Неизвестно")
        print(
            f"{transaction['id']}. "
            f"Сумма: {transaction['amount']}, "
            f"Категория: {category_name}, "
            f"Заметки: {transaction['note']}, "
            f"Дата: {transaction['date']}"
        )


def add_transaction(operation="-"):
    categories = load_file(FILE_CATEGORIES)

    if not categories and operation != "+":
        print("Действие недоступно. Пока нет категорий.")
        return

    try:
        amount = int(input("Введите сумму операции: "))
    except ValueError:
        print("Ошибка: введите число.")
        return

    if operation != "+":
        show_categories()
        id_category = found_category()
    else:
        id_category = 0

    add_to_balance(id_category, amount)

    note = input("Введите комментарий (необязательно): ")

    history = load_file(FILE_HISTORY)
    id_history = (max((item["id"] for item in history), default=0)) + 1
    date = datetime.date.today().isoformat()

    history.append(
        {
            "id": id_history,
            "amount": amount,
            "id_category": id_category,
            "note": note,
            "date": date,
        }
    )

    save_file(FILE_HISTORY, history)
    print("Операция добавлена!")


def found_transaction():
    history = load_file(FILE_HISTORY)

    while True:
        try:
            id_transaction = int(input("Введите ID операции: "))
        except ValueError:
            print("Ошибка: введите число.")
            continue

        if any(item.get("id") == id_transaction for item in history):
            return id_transaction
        else:
            print("Такой операции не существует, попробуйте еще раз.")


def edit_transaction():
    history = load_file(FILE_HISTORY)
    categories = load_file(FILE_CATEGORIES)

    if not history:
        print("Действие недоступно. Пока нет операций.")
        return

    print("Изменение операции")
    id_transaction = found_transaction()
    show_categories()

    id_category = int(input("Введите новую категорию для операции: "))
    amount = int(input("Введите новую сумму для операции: "))

    for transaction in history:
        if transaction["id"] == id_transaction:
            delete_from_balance(transaction["id_category"], transaction["amount"])
            transaction["id_category"] = id_category
            transaction["amount"] = amount
            add_to_balance(id_category, amount)
            break

    save_file(FILE_HISTORY, history)

    category_name = categories[id_category]["category_name"]
    print(f"Операция успешно изменена на {amount} в категории '{category_name}'.")


def delete_transaction():
    history = load_file(FILE_HISTORY)

    if not history:
        print("Действие недоступно. Пока нет операций.")
        return

    id_transaction = found_transaction()

    for index, transaction in enumerate(history):
        if transaction["id"] == id_transaction:
            delete_from_balance(transaction["id_category"], transaction["amount"])
            del history[index]
            save_file(FILE_HISTORY, history)
            print(f"Операция с ID {id_transaction} успешно удалена.")
            return

    print(f"Операция с ID {id_transaction} не найдена.")


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
