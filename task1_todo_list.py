import json

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks):
    title = input("Enter the task title: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{idx}. {task['title']} - {status}")

def update_task(tasks):
    view_tasks(tasks)
    task_no = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_no < len(tasks):
        title = input("Enter the new title: ")
        tasks[task_no]["title"] = title
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_no = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks.pop(task_no)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def mark_task_completed(tasks):
    view_tasks(tasks)
    task_no = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks[task_no]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_task_completed(tasks)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
