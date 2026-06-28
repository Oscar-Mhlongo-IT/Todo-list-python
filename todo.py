tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to remove: "))
            if 0 < index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid number")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
