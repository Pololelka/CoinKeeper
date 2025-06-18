from models.category_model import get_expense_categories, get_all_categories
from models.transaction_model import get_all_history


def input_id_category():
    categories = get_expense_categories()
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


def input_id_transaction():
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


def input_amount():
    while True:
        try:
            amount = int(input("Введите сумму операции: "))
            return amount
        except ValueError:
            print("Ошибка: введите число.")
            continue


def input_category_name():
    while True:
        category_name = input("Введите название категории: ").strip()

        categories = get_all_categories()
        if not category_name:
            print("Ошибка: название не может быть пустым.")
        elif any(
            c["category_name"].lower() == category_name.lower() for c in categories
        ):
            print(f"Категория «{category_name}» уже существует.")
        else:
            return category_name


def input_choise_menu():
    while True:
        try:
            choice = int(input("\nВыберите действие: "))
            return choice
        except ValueError:
            print("Ошибка: введите число.")
            continue
