from Task import Task
from UrgentTask import UrgentTask
from utils import validate_date, get_valid_input, validate_status, validate_priority


tasks = []


def add_task():
  title = get_valid_input("Enter task title ")
  description = get_valid_input("Enter task description ")
  due_date =validate_date("Enter the  date ")
  is_urgent_input = get_valid_input("Is this task urgent? (yes/no): ").strip().lower()
  if is_urgent_input in ['yes', 'y','ye']:
        priority = validate_priority("Enter the priority (High/Medium/Low)  ")
        task = UrgentTask(title, description, due_date, priority)
        tasks.append(task)
  else:
    task = Task(title, description, due_date)
    tasks.append(task)
  print("Task added successfully.")



  
def view_tasks():
    if len(tasks) != 0:
        for task in tasks:
            print(task.display())
    else:
        print("No tasks added yet.")


def delete_task():
    task_idd = int(get_valid_input("Enter task ID to delete: "))
    for task in tasks:
        if task.task_id == task_idd:
            tasks.remove(task)
            print("Task deleted successfully.")
            break 
        else:
            print(f"Task not found.{task.task_id} ") 


def update_task():
    task_id =int( get_valid_input("Enter task ID to update: "))
    for task in tasks:
        if task.task_id == task_id:
            title = get_valid_input("Enter new title ")
            description = get_valid_input("Enter new description  ")
            due_date= validate_date("Enter new due date (YYYY-MM-DD) ")
            status = validate_status("Enter new status (InProgress/Completed)")
          

            task.update_details(
                title if title else None,
                description if description else None,
                due_date if due_date else None,
                status if status else None
            )
            print("Task updated successfully.")
            break

    
    print("Task not found.")


def Menu():
    while True:
        print("Task Manager Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = get_valid_input("Enter your choice: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
Menu()
# view_tasks()
# add_task()
# view_tasks()
# update_task()
# view_tasks()
# delete_task()