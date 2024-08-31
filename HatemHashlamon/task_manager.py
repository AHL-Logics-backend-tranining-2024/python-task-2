from typing import List
from task import *
from utils import *

# List to store all tasks (including urgent tasks)
tasks: List[Task] = []

def display_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    try:
        task_id = len(tasks) + 1
        title = get_valid_input("Enter task title: ")
        description = get_valid_input("Enter task description: ")
        due_date = get_valid_input("Enter due date (YYYY-MM-DD): ")
        validate_date(due_date)  
        status = get_valid_input("Enter task status (InProgress/Completed): ")
        validate_status(status) 

        is_urgent = get_valid_input("Is this task urgent? (yes/no): ").strip().lower()
        if is_urgent.lower() in ["yes", "y"]:
            priority = get_valid_input("Enter priority (High/Medium/Low): ")
            validate_priority(priority)  
            task = UrgentTask(task_id, title, description, due_date, status, priority)
        else:
            task = Task(task_id, title, description, due_date, status)
        
        tasks.append(task)
        print("Task added.")
    except ValueError as e:
        print(e)


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    regular_tasks = [task for task in tasks if not isinstance(task, UrgentTask)]
    urgent_tasks = [task for task in tasks if isinstance(task, UrgentTask)]

    if regular_tasks:
        print("\nTasks:")
        for task in regular_tasks:
            print(task.display() + '\n')
    
    if urgent_tasks:
        print("\nUrgent Tasks:")
        for task in urgent_tasks:
            print(task.display() + '\n')
                
def update_task():
    try:
        task_id = int(get_valid_input("Enter task ID to update: "))
        task = next((t for t in tasks if t.task_id == task_id), None)

        if task is None:
            print("Task not found.")
            return

        title = get_valid_input(f"Enter new title (current: {task.title}): ")
        description = get_valid_input(f"Enter new description (current: {task.description}): ")
        due_date = get_valid_input(f"Enter new due date (current: {task.due_date}): ")
        validate_date(due_date)
        status = get_valid_input(f"Enter new status (current: {task.status}): ")
        validate_status(status) 

        priority = None
        if isinstance(task, UrgentTask):
            priority = get_valid_input(f"Enter new priority (current: {task.priority}): ")
            validate_priority(priority)

        task.update_details(
            title=title if title else None,
            description=description if description else None,
            due_date=due_date if due_date else None,
            status=status if status else None,
            priority=priority if priority else None
        )

        print("Task updated.")
    except ValueError as e:
        print(e)


def delete_task():
    pass

def main():
    while True:
        display_menu()
        choice = get_valid_input("Choose an option: ")
        
        match choice:
            case "1":
                add_task()
            case "2":
                view_tasks()
            case "3":
                update_task()
            case "4":
                delete_task()
            case "5":
                break
            case _:
                print("Invalid choice. Please try again.")

