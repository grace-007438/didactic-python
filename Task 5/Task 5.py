# To-Do List Application

tasks = []

while True:
    print("\n")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Delete Task")
    print("4.Exit")

    option = input("Enter your option (1-4): ")

    if option == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif option == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif option == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number.")

    elif option == "4":
        print("Exiting the To-Do List. Goodbye!")
        break

    else:
        print("Invalid option. Please select 1-4.")
