from models.balance_model import update_balance, get_balance


def add_to_balance(id_category, amount):
    balance = get_balance()
    balance += -amount if id_category != 1 else amount
    update_balance(balance)


def delete_from_balance(id_category, amount):
    balance = get_balance()
    balance += amount if id_category != 1 else -amount
    update_balance(balance)
