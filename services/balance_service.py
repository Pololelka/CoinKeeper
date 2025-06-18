from models.balance_model import update_balance, get_balance
from config import INCOME_CATEGORY_ID


def add_to_balance(id_category, amount):
    balance = get_balance()
    if id_category != INCOME_CATEGORY_ID:
        balance -= amount
    else:
        balance += amount
    update_balance(balance)


def delete_from_balance(id_category, amount):
    balance = get_balance()
    if id_category != INCOME_CATEGORY_ID:
        balance += amount
    else:
        balance -= amount
    update_balance(balance)
