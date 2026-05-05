import json
import os

TASKS_FILE = "tasks.json"


def load_tasks(filename=TASKS_FILE):
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks, filename=TASKS_FILE):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description, filename=TASKS_FILE):
    tasks = load_tasks(filename)

    task = {
        "id": len(tasks) + 1,
        "description": description,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks, filename)
    return task


def view_tasks(filename=TASKS_FILE):
    tasks = load_tasks(filename)

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "Done" if task["completed"] else "Not Done"
        print(f'{task["id"]}. {task["description"]} - {status}')


def mark_task_complete(task_id, filename=TASKS_FILE):
    tasks = load_tasks(filename)

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks, filename)
            return True

    return False


def delete_task(task_id, filename=TASKS_FILE):
    tasks = load_tasks(filename)
    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(updated_tasks) == len(tasks):
        return False

    for index, task in enumerate(updated_tasks, start=1):
        task["id"] = index

    save_tasks(updated_tasks, filename)
    return True


def menu():
    while True:
        print("\nTask Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks()

        elif choice == "2":
            description = input("Enter task description: ")
            add_task(description)
            print("Task added.")

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark complete: "))
                if mark_task_complete(task_id):
                    print("Task marked complete.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                if delete_task(task_id):
                    print("Task deleted.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
