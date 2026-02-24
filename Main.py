import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()

def add_task(tasks):
    task_name = input("Enter task: ")
    tasks.append(task_name + " | Pending")
    print("Task added.\n")

def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark complete: "))
        tasks[task_number - 1] = tasks[task_number - 1].replace("Pending", "Done")
        print("Task marked as completed.\n")
    except:
        print("Invalid selection.\n")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to delete: "))
        tasks.pop(task_number - 1)
        print("Task deleted.\n")
    except:
        print("Invalid selection.\n")

def main():
    tasks = load_tasks()
    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()