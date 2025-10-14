# Task 4: Simple To-Do List

tasks = []  # Empty list to store tasks

def show_menu():
    print("\n=== Simple To-Do List ===")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter task to add: ")
        tasks.append(task)
        print(f"✅ '{task}' added to the list.")

    elif choice == '2':
        print("\n📝 Your Tasks:")
        if not tasks:
            print("No tasks added yet.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == '3':
        print("\n🗑️ Remove Task:")
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"❌ '{removed}' removed from the list.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        print("👋 Exiting To-Do List. Have a productive day!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
