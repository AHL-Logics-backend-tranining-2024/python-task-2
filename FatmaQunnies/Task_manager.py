from FatmaQunnies.Task import Task
from FatmaQunnies.UrgentTask import UrgentTask
from FatmaQunnies.utils import validate_date, get_valid_input, validate_status, validate_priority


tasks = []


def add_task():
  title = get_valid_input("Enter task title ")
  description = get_valid_input("Enter task description")
  due_date =validate_date("Enter the  date")
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
    for task in tasks:
        print(task.display())
       



def delete_task():
    task_id = get_valid_input("Enter task ID to delete: ")
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            print("Task deleted successfully.")
            return
    print("Task not found.") 


def update_task():
    task_id = get_valid_input("Enter task ID to update: ")
    for task in tasks:
        if task.task_id == task_id:
            title = get_valid_input("Enter new title ")
            description = get_valid_input("Enter new description  ")
            due_date = get_valid_input("Enter new due date (YYYY-MM-DD) ")
            if due_date:
                validate_date(due_date)
            status = get_valid_input("Enter new status (InProgress/Completed)")
            if status:
                validate_status(status)

            task.update_details(
                title if title else None,
                description if description else None,
                due_date if due_date else None,
                status if status else None
            )

    
    print("Task not found.")
