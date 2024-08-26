from task import Task
from urgent_task import UrgentTask
from utils import validate_date, get_valid_input, validate_status, validate_priority

tasks = []

def add_task():
    try:
        
            while True:
                title_input = input("Enter task title: ").strip()
                title = get_valid_input(title_input)
                if title:
                    break
                print("Title cannot be empty. Please try again.")

            while True:
                description_input = input("Enter task description: ").strip()
                description = get_valid_input(description_input)
                if description:
                    break
                print("Description cannot be empty. Please try again.")

            while True:
                date_str = input("Enter the due date (YYYY-MM-DD): ").strip()
                due_date = validate_date(date_str)
                if due_date:
                    break
                print("Invalid date. Please try again.")

            while True:
              is_urgent_inputt = input("Is this task urgent? (yes/no): ").strip()
              is_urgent_input = get_valid_input(is_urgent_inputt)
              if is_urgent_input and is_urgent_input.strip().lower() in ['yes', 'y', 'no', 'n']:
                is_urgent_input = is_urgent_input.strip().lower()
                break
              print("Invalid input. Please enter 'yes' or 'no'.")

            if is_urgent_input in ['yes', 'y']:
                while True:
                    priority_input = input("Enter the priority (High/Medium/Low): ").strip().lower()
                    priority = validate_priority(priority_input)
                    if priority:
                        break
                    print("Invalid priority. Please enter 'High', 'Medium', or 'Low'.")
                task = UrgentTask(title, description, due_date, priority)
            else:
                task = Task(title, description, due_date)

            tasks.append(task)
            print("Task added successfully.")
           
    
    except Exception as e:
        print(f"An error occurred: {e}")

def view_tasks():
    if len(tasks) != 0: 
        for task in tasks:
            print(task.display())
    else:
        print("No tasks added yet.")

def delete_task():
    try:
        while True:
            task_idd_input = input("Enter task ID to delete: ").strip()
            task_idd = int(get_valid_input(task_idd_input))
            if task_idd:
                break
            print("Invalid task ID. Please try again.")
        
        for task in tasks:
            if task.task_id == task_idd:
                tasks.remove(task)
                print("Task deleted successfully.")
                return
        print("Task not found.") 
    
    except Exception as e:
        print(f"An error occurred: {e}")

def update_task():
    try:
        while True:
            task_idd_input = input("Enter task ID to update: ").strip()
            task_id = int(get_valid_input(task_idd_input))
            if task_id:
                break
            print("Invalid task ID. Please try again.")
        
        for task in tasks:
            if task.task_id == task_id:
                while True:
                    title_input = input("Enter new title: ").strip()
                    title = get_valid_input(title_input)
                    if title:
                        break
                    print("Title cannot be empty. Please try again.")
                
                while True:
                    description_input = input("Enter new description: ").strip()
                    description = get_valid_input(description_input)
                    if description:
                        break
                    print("Description cannot be empty. Please try again.")

                while True:
                    due_date_input = input("Enter new due date (YYYY-MM-DD): ").strip()
                    due_date = validate_date(due_date_input)
                    if due_date:
                        break
                    print("Invalid date. Please try again.")

                while True:
                    status_input = input("Enter new status (InProgress/Completed): ").strip()
                    status = validate_status(status_input)
                    if status:
                        break
                    print("Invalid status. Please enter 'InProgress' or 'Completed'.")

                task.update_details(
                    title if title else None,
                    description if description else None,
                    due_date if due_date else None,
                    status if status else None
                )
                print("Task updated successfully.")
                return
        
        print("Task not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")


def Menu():
    while True:
        print("Task Manager Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        try:
            task_input = input("Enter your choice: ").strip()
            choice = get_valid_input(task_input)
            
            match choice:
                case '1':
                    add_task()
                case '2':
                    view_tasks()
                case '3':
                    update_task()
                case '4':
                    delete_task()
                case '5':
                    break
                case _:
                    print("Invalid choice. Please try again.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

Menu()
