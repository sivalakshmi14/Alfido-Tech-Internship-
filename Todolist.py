# Simple To-Do List App

todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added successfully!")

def remove_task(task_number):
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task number!")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Main program loop
while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")