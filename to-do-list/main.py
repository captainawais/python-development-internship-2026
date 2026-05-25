# =========================================================
# ADVANCED TO-DO LIST APPLICATION
# Developed in Python
# =========================================================

import os

TASK_FILE = "tasks.txt"


# =========================================================
# LOAD TASKS
# =========================================================
def load_tasks():

    if not os.path.exists(TASK_FILE):
        return []

    with open(TASK_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]

    return tasks


# =========================================================
# SAVE TASKS
# =========================================================
def save_tasks(tasks):

    with open(TASK_FILE, "w") as file:

        for task in tasks:
            file.write(task + "\n")


# =========================================================
# DISPLAY HEADER
# =========================================================
def display_header():

    print("\n" + "=" * 55)
    print("         ADVANCED TO-DO LIST APPLICATION")
    print("=" * 55)


# =========================================================
# DISPLAY MENU
# =========================================================
def display_menu():

    print("\nSelect an Option:")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Clear All Tasks")
    print("7. Exit")


# =========================================================
# VIEW TASKS
# =========================================================
def view_tasks(tasks):

    print("\n" + "-" * 55)
    print("                    YOUR TASKS")
    print("-" * 55)

    if not tasks:
        print("No tasks available.\n")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print("-" * 55)


# =========================================================
# ADD MULTIPLE TASKS
# =========================================================
def add_task(tasks):

    try:

        total_tasks = int(
            input("\nHow many tasks do you want to add: ")
        )

        for i in range(total_tasks):

            task_name = input("Enter the task: ").strip()

            if task_name == "":
                print("Task cannot be empty.")
                continue

            new_task = f"[ ] {task_name}"

            tasks.append(new_task)

            print("Task added!")

        save_tasks(tasks)

    except ValueError:
        print("Please enter a valid number.")
        
# =========================================================
# COMPLETE TASK
# =========================================================
def complete_task(tasks):

    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:

        task_number = int(input("\nEnter task number to complete: "))

        if 1 <= task_number <= len(tasks):

            current_task = tasks[task_number - 1]

            if current_task.startswith("[✔]"):
                print("Task already completed.")
            else:

                updated_task = current_task.replace("[ ]", "[✔]")

                tasks[task_number - 1] = updated_task

                save_tasks(tasks)

                print("Task marked as completed!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# =========================================================
# DELETE TASK
# =========================================================
def delete_task(tasks):

    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:

        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):

            deleted_task = tasks.pop(task_number - 1)

            save_tasks(tasks)

            print(f"Deleted Task: {deleted_task}")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# =========================================================
# SEARCH TASK
# =========================================================
def search_task(tasks):

    keyword = input("\nEnter keyword to search: ").lower()

    found_tasks = []

    for index, task in enumerate(tasks, start=1):

        if keyword in task.lower():
            found_tasks.append((index, task))

    print("\nSearch Results:")
    print("-" * 55)

    if found_tasks:

        for index, task in found_tasks:
            print(f"{index}. {task}")

    else:
        print("No matching task found.")

    print("-" * 55)


# =========================================================
# CLEAR ALL TASKS
# =========================================================
def clear_all_tasks(tasks):

    confirmation = input(
        "\nAre you sure you want to delete all tasks? (yes/no): "
    ).lower()

    if confirmation == "yes":

        tasks.clear()

        save_tasks(tasks)

        print("All tasks deleted successfully!")

    else:
        print("Operation cancelled.")


# =========================================================
# MAIN APPLICATION
# =========================================================
def main():

    tasks = load_tasks()

    while True:

        display_header()

        display_menu()

        choice = input("\nEnter your choice: ")

        # ADD TASK
        if choice == "1":
            add_task(tasks)

        # VIEW TASKS
        elif choice == "2":
            view_tasks(tasks)

        # COMPLETE TASK
        elif choice == "3":
            complete_task(tasks)

        # DELETE TASK
        elif choice == "4":
            delete_task(tasks)

        # SEARCH TASK
        elif choice == "5":
            search_task(tasks)

        # CLEAR ALL TASKS
        elif choice == "6":
            clear_all_tasks(tasks)

        # EXIT APPLICATION
        elif choice == "7":

            print("\nThank you for using the application.")
            print("Goodbye!\n")

            break

        else:
            print("Invalid option. Please try again.")


# =========================================================
# RUN APPLICATION
# =========================================================
if __name__ == "__main__":
    main()