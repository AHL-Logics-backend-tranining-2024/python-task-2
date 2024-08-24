from task import Task, UrgentTask
from utils import validate_date, get_valid_input, validate_status, validate_priority, save_tasks_to_file, load_tasks_from_file

tasks, urgent_tasks = load_tasks_from_file()

def add_task():
    title = get_valid_input("Enter task title: ")
    description = get_valid_input("Enter task description: ")
    due_date = get_valid_input("Enter due date (YYYY-MM-DD): ")
    
    if not validate_date(due_date):
        return
    
    is_urgent = input("Is this an urgent task? (yes/no): ").lower()
    if is_urgent in ['yes', 'y']:
        priority = get_valid_input("Enter task priority (High/Medium/Low): ")
        if not validate_priority(priority):
            return
        task = UrgentTask(title, description, due_date, priority)
        urgent_tasks.append(task)
    else:
        task = Task(title, description, due_date)
        tasks.append(task)
    
    save_tasks_to_file(tasks, urgent_tasks)
    print("Task added successfully!")

def view_tasks():
    print("\n--- Urgent Tasks ---")
    for task in urgent_tasks:
        print(task.display())
    
    print("\n--- Regular Tasks ---")
    for task in tasks:
        print(task.display())

def update_task():
    task_id = int(input("Enter the task ID to update: "))
    task_found = False

    for task in tasks + urgent_tasks:
        if task.task_id == task_id:
            task_found = True
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            due_date = input("Enter new due date (YYYY-MM-DD, leave blank to keep current): ")
            status = input("Enter new status (InProgress/Completed, leave blank to keep current): ")

            if due_date and not validate_date(due_date):
                return
            if status and not validate_status(status):
                return
            
            task.update_details(title, description, due_date, status)
            save_tasks_to_file(tasks, urgent_tasks)
            print("Task updated successfully!")
            break

    if not task_found:
        print("Task not found!")

def delete_task():
    task_id = int(input("Enter the task ID to delete: "))
    global tasks, urgent_tasks

    tasks = [task for task in tasks if task.task_id != task_id]
    urgent_tasks = [task for task in urgent_tasks if task.task_id != task_id]

    save_tasks_to_file(tasks, urgent_tasks)
    print("Task deleted successfully!")

def main_menu():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks_to_file(tasks, urgent_tasks)
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
