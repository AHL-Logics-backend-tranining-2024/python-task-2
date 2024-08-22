from task import Task
from urgent_task import UrgentTask
from utils import validate_date, get_valid_input, validate_status, validate_priority


tasks = []
 

def add_task():
  title_input = input("Enter task title ").strip()
  title = get_valid_input(title_input)
  description_input = input("Enter task description ").strip()
  description = get_valid_input(description_input)
  date_str = input("Enter the  date ")
  due_date =validate_date(date_str)
  is_urgent_inputt = input("Is this task urgent? (yes/no): ").strip()
  is_urgent_input = get_valid_input(is_urgent_inputt).strip().lower()
  if is_urgent_input in ['yes', 'y','ye']:
        priority_input = input("Enter the priority (High/Medium/Low)  ").strip()
        priority = validate_priority(priority_input)
        task = UrgentTask(title, description, due_date, priority)
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
    task_idd_input = input("Enter task ID to delete:  ").strip()
    task_idd = int(get_valid_input(task_idd_input))
    for task in tasks:
        if task.task_id == task_idd:
            tasks.remove(task)
            print("Task deleted successfully.")
            break 
        else:
            print(f"Task not found.{task.task_id} ") 


def update_task():
    task_idd_input = input("Enter task ID to update: ").strip()

    task_id =int( get_valid_input(task_idd_input ))
    for task in tasks:
        if task.task_id == task_id:
            title_input = input("Enter new title ").strip()
            title = get_valid_input(title_input)
            description_input = input("Enter new description  ").strip()
            description = get_valid_input(description_input)
            due_date_input = input("Enter new due date (YYYY-MM-DD) ").strip()
            due_date= validate_date(due_date_input)
            status_input = input("Enter new status (InProgress/Completed)").strip()
            status = validate_status(status_input)
          

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
        
        task_input = input("Enter your choice: ").strip()
        choice = get_valid_input(task_input)
        
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
