import os

TASKS_FILE = "tasks.txt"

# Ensure tasks file exists
def ensure_file_exists():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as file:
            pass  # Create an empty file

# Load tasks from the file
def load_tasks():
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

# Save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add a task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available!")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

# Update a task
def update_task(tasks):
    if not tasks:
        print("No tasks available to update!")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_num - 1] = new_task
            print("Task updated!")
        else:
            print("Invalid task number! Returning to main menu.")
    except ValueError:
        print("Invalid input! Please enter a number. Returning to main menu.")

# Delete a task
def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete!")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("Task deleted!")
        else:
            print("Invalid task number! Returning to main menu.")
    except ValueError:
        print("Invalid input! Please enter a number. Returning to main menu.")

# Main program
def main():
    ensure_file_exists()  # Ensure file is created if not present
    tasks = load_tasks()  # Load tasks from file
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
