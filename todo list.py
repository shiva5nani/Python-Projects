def add_task(task_list):
    description = input("Enter the task: ")
    task = {
        "task": description,
        "done": False
    }
    task_list.append(task)
    print("Task added successfully.")


def show_tasks(task_list):
    if len(task_list) == 0:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(task_list, start=1):
            status = "Completed" if task["done"] else "Not Completed"
            print(f"{i}. {task['task']} - {status}")


def complete_task(task_list):
    show_tasks(task_list)
    if len(task_list) == 0:
        return

    try:
        number = int(input("Enter task number to mark as completed: "))
        if 1 <= number <= len(task_list):
            task_list[number - 1]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = []

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


main()
