from services.transactions_service import (
    show_history,
    add_transaction,
    delete_transaction,
    edit_amount_transaction,
    edit_category_transaction,
)


def edit_transaction_menu():
    while True:
        print("\n1. Редактировать сумму")
        print("2. Редактировать категорию")
        print("0. Назад")

        edit_choice = input("\nВыберите действие: ")
        show_history()
        if edit_choice == "1":
            edit_amount_transaction()
            break
        elif edit_choice == "2":
            edit_category_transaction()
            break
        elif edit_choice == "0":
            print("Назад")
            break


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
            add_transaction("expense")
        elif choice == "2":
            add_transaction("income")
        elif choice == "3":
            edit_transaction_menu()
        elif choice == "4":
            delete_transaction()
        elif choice == "0":
            print("Назад")
            break
