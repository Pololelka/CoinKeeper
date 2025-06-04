from storage import load_file, save_file

FILE_BALANCE = "data/balance.json"


def add_to_balance(id_catogory, amount):
    balance = load_file(FILE_BALANCE)
    balance[0]["balance"] += -amount if id_catogory != 0 else amount
    save_file(FILE_BALANCE, balance)


def delete_from_balance(id_catogory, amount):
    balance = load_file(FILE_BALANCE)
    balance[0]["balance"] += amount if id_catogory != 0 else -amount
    save_file(FILE_BALANCE, balance)


def show_balance():
    balance = load_file(FILE_BALANCE)
    return balance[0]["balance"]
