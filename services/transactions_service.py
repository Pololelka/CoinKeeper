import datetime
from services.categories_service import (
    show_categories,
    get_dict_categories,
    check_categories,
)
from services.balance_service import add_to_balance, delete_from_balance
from models.transaction_model import (
    get_all_history,
    get_transaction_by_id,
    update_history,
    delete_from_history,
    insert_to_history,
)

from utils.input_helpers import input_id_transaction, input_id_category, input_amount
from config import INCOME_CATEGORY_ID


def show_history():
    if not check_transaction_history():
        return
    history = get_all_history()
    category_dict = get_dict_categories()

    print("История операций:\n")
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


def add_transaction(operation="expense"):
    if not check_categories():
        return

    amount = input_amount()

    if operation != "income":
        show_categories()
        id_category = input_id_category()
    else:
        id_category = INCOME_CATEGORY_ID

    add_to_balance(id_category, amount)

    note = input("Введите комментарий (необязательно): ")
    date = datetime.date.today().isoformat()
    insert_to_history(amount, id_category, note, date)

    print("Операция добавлена!")


def edit_amount_transaction():
    if not check_transaction_history():
        return

    print("Изменение суммы операции")
    id_transaction = input_id_transaction()
    amount = input_amount()

    old_transaction = get_transaction_by_id(id_transaction)

    update_history(amount, old_transaction["id_category"], id_transaction)

    delete_from_balance(old_transaction["id_category"], old_transaction["amount"])
    add_to_balance(old_transaction["id_category"], amount)

    print(f"Сумма операции успешно изменена на {amount}.")


def edit_category_transaction():
    if not check_transaction_history():
        return

    if not check_categories():
        return

    print("Изменение категории операции")
    id_transaction = input_id_transaction()
    show_categories()

    id_category = input_id_category()

    old_transaction = get_transaction_by_id(id_transaction)

    update_history(old_transaction["amount"], id_category, id_transaction)

    delete_from_balance(old_transaction["id_category"], old_transaction["amount"])
    add_to_balance(id_category, old_transaction["amount"])
    category_dict = get_dict_categories()

    category_name = category_dict.get(id_category, "Неизвестно")

    print(f"Категория успешно изменена на '{category_name}'.")


def delete_transaction():
    if not check_transaction_history():
        return

    id_transaction = input_id_transaction()
    transaction = get_transaction_by_id(id_transaction)

    delete_from_history(id_transaction)
    delete_from_balance(transaction["id_category"], transaction["amount"])
    print(f"Операция с ID {id_transaction} успешно удалена.")


def check_transaction_history():
    history = get_all_history()
    if not history:
        print("Действие недоступно. Пока нет операций.")
        return False
    return True
