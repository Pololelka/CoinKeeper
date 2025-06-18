from models.category_model import (
    get_all_categories,
    get_category_by_id,
    insert_to_categories,
    update_categories,
    get_expense_categories,
)
from utils.input_helpers import input_id_category


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
    categories = get_expense_categories()
    if not categories:
        print("Пока нет категорий.")
        return

    print("Ваши категории:")
    for category in categories:
        print(f"{category['id_category']}. {category['category_name']}")


def edit_categories():
    categories = get_expense_categories()
    if not categories:
        print("Действие недоступно. Пока нет категорий расхода.")
        return

    print("Изменение категории")
    id_category = input_id_category()
    new_name = input("Введите новое название категории: ").strip()

    old_name = get_category_by_id(id_category)
    update_categories(new_name, id_category)

    print(f"Категория «{old_name['category_name']}» была изменена на «{new_name}».")


def get_dict_categories():
    categories = get_all_categories()
    category_dict = {cat["id_category"]: cat["category_name"] for cat in categories}
    return category_dict
