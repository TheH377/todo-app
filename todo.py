import json
import os

FILENAME = "tasks.json"

def load_tasks():
    """Загружает задачи из JSON-файла."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """Сохраняет задачи в JSON-файл."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def show_tasks(tasks):
    """Выводит список задач."""
    if not tasks:
        print("\nСписок задач пуст!")
        return
    
    print("\n--- ТВОЙ СПИСОК ЗАДАЧ ---")
    for i, task in enumerate(tasks, 1):
        status = "[✓]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['title']}")
    print("-" * 25)

def add_task(tasks):
    """Добавляет новую задачу."""
    title = input("Введите название задачи: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print(f'Задача "{title}" успешно добавлена!')
    else:
        print("Название задачи не может быть пустым.")

def mark_done(tasks):
    """Отмечает задачу как выполненную."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Введите номер выполненной задачи: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print(f'Задача "{tasks[index]["title"]}" отмечена как выполненная!')
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите число.")

def delete_task(tasks):
    """Удаляет задачу."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f'Задача "{removed["title"]}" удалена!')
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите число.")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== МЕНЕДЖЕР ЗАДАЧ ===")
        print("1. Посмотреть задачи")
        print("2. Добавить задачу")
        print("3. Отметить как выполненную")
        print("4. Удалить задачу")
        print("5. Выход")
        
        choice = input("Выберите действие (1-5): ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()