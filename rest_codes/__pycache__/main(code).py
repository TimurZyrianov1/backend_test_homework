import os

# Путь к корневой директории проекта
project_root = "character_creation_module"

# Функция для рекурсивного просмотра структуры директории
def print_directory_structure(path, indent=""):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(indent + f"├── {item}/")
            print_directory_structure(item_path, indent + "│   ")
        else:
            print(indent + f"├── {item}")

# Вывести структуру проекта, начиная с корневой директории
print_directory_structure(project_root)
