# Simple To-Do List App (Console Version)

todo_list = []

def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task to add: ")
    todo_list.append(task)
    print(f"'{task}' has been added to your to-do list.")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the task number to remove: "))
            removed = todo_list.pop(task_num - 1)
            print(f"'{removed}' has been removed from your to-do list.")
        except (IndexError, ValueError):
            print("Invalid task number. Please try again.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")