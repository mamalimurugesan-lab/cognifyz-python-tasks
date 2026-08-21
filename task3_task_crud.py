# Cognifyz Task 3 - Basic Task CRUD Application

tasks = []

def create_task():
    title = input("Enter task title: ").strip()
    if title:
        tasks.append(title)
        print("Task added successfully!")
    else:
        print("Task title cannot be empty.")

def read_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def update_task():
    read_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to update: "))

        if 1 <= number <= len(tasks):
            new_title = input("Enter the new task title: ").strip()

            if new_title:
                tasks[number - 1] = new_title
                print("Task updated successfully!")
            else:
                print("Task title cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    read_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted = tasks.pop(number - 1)
            print(f"Task '{deleted}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n" + "=" * 40)
    print("          TASK MANAGER")
    print("=" * 40)
    print("1. Create Task")
    print("2. Read Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        create_task()
    elif choice == "2":
        read_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank you for using Task Manager!")
        break
    else:
        print("Invalid choice. Please select 1-5.")
