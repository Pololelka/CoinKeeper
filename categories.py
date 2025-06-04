from storage import load_file, save_file

FILE_CATEGORIES = "data/categories.json"


def add_category():
    print("\nДобавление новой категории")
    name = input("Введите название категории: ").strip()

    if not name:
        print("Ошибка: название не может быть пустым.")
        return

    categories = load_file(FILE_CATEGORIES)

    if any(c["category_name"].lower() == name.lower() for c in categories):
        print(f"Категория «{name}» уже существует.")
        return

    new_id = max((c["id"] for c in categories), default=0) + 1
    categories.append({"id": new_id, "category_name": name})
    save_file(FILE_CATEGORIES, categories)
    print(f"Категория «{name}» добавлена!")


def show_categories():
    categories = load_file(FILE_CATEGORIES)

    visible_categories = [c for c in categories if c["id"] != 0]

    if not visible_categories:
        print("Пока нет категорий.")
        return

    print("Ваши категории:")
    for category in visible_categories:
        print(f"{category['id']}. {category['category_name']}")


def edit_categories():
    categories = load_file(FILE_CATEGORIES)

    if not categories:
        print("Действие недоступно. Пока нет категорий.")
        return

    print("Изменение категории")
    id_category = found_category()
    new_name = input("Введите новое название категории: ").strip()

    for category in categories:
        if category["id"] == id_category:
            old_name = category["category_name"]
            category["category_name"] = new_name
            save_file(FILE_CATEGORIES, categories)
            print(f"Категория «{old_name}» была изменена на «{new_name}».")
            return


def found_category():
    categories = load_file(FILE_CATEGORIES)

    while True:
        try:
            id_category = int(input("Введите ID категории: "))
        except ValueError:
            print("Ошибка: введите число.")
            continue

        if any(item.get("id") == id_category for item in categories):
            return id_category
        else:
            print("Такой категории не существует, попробуйте ещё раз.")


def categories_menu():
    while True:
        show_categories()
        print("\n1. Добавить категорию")
        print("2. Изменить категорию")
        print("0. Назад")

        choice = input("\nВыберите действие: ")

        if choice == "1":
            add_category()
            show_categories()
        elif choice == "2":
            edit_categories()
        elif choice == "0":
            print("Назад")
            break
