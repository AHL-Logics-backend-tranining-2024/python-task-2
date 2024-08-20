import utils
from task import Task
from urgentTask import UrgentTask
import json


tasks = []


def menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Search Task by status")
    print("6. Exit")


# This function add new task by taking user inputs  and validate each input so only valid data is accepted.
# The task is then saved to either the regular task list or the urgent task list, depending on whether it is marked as urgent.
def add_task():
    # Loop until valid data is entered for the title
    while True:
        title = input("Enter your task title: ")
        try:
            utils.get_valid_input(title)
            break # break only when validation function return True
        except ValueError as e:
            print(e) 

    while True:
        description = input("Enter task description: ")
        try:
            utils.get_valid_input(description)
            break
        except ValueError as e:
            print(e)

    while True:
        due_date = input("Enter task due_date (in YYYY-MM-DD format): ")
        try:
            utils.validate_date(due_date)
            break
        except ValueError as e:
            print(e)
    while True:
        status = input("Enter task status (InProgress , Completed): ").strip().lower()
        try:
            utils.validate_status(status)
            break
        except ValueError as e:
            print(e)

    is_urgent = input("is the task urgent(yes/no) ? ").strip().lower()
    if is_urgent in ['yes' ,'y']:
        while True:
            priority = input("Enter task priority (High/Medium/Low): ").strip().lower()
            try:
                utils.validate_priority(priority)
                break
            except ValueError as e:
                print(e)
        task_instance = UrgentTask(priority ,title,description,due_date,status)
        tasks.append(task_instance)
        print("Urgent task successfully created.")
        main()
    else :
        task_instance = Task(title,description,due_date,status)
        tasks.append(task_instance)
        print("task successfully created")
        main()

def view_tasks():
    if not tasks:
        print("🚫 No tasks available. 🚫")
    else:
        urgent_tasks = [task for task in tasks if isinstance(task, UrgentTask)]
        regular_tasks = [task for task in tasks if isinstance(task, Task) and not isinstance(task, UrgentTask)]

        if urgent_tasks:
            print("\n" + "="*30)
            print("🚨🚨🚨 Urgent Tasks 🚨🚨🚨")
            print("="*30)
            for task in urgent_tasks:
                task.display()
                print("\n")

            print("\n")
        if regular_tasks:
            print("\n" + "-"*30)
            print("📝📝📝 Regular Tasks 📝📝📝")
            print("-"*30)
            for task in regular_tasks:
                task.display()
                print("\n")
    main()


# This function find a specific task in tasks list and return it to make operation on it 
def find_task_by_id(id):
    for task in tasks :
        if task.task_id == id:
            return task
    raise ValueError("Task with the provided ID does not exist.")

# This function update details for any task
def update_task():
    task_id = input("Please Enter the Task ID you want to update: ").strip()
    try:
        task_to_update = find_task_by_id(task_id)        
        print("\nPlease provide the new details. Leave blank if you don't want to change a specific field.") 
        new_title = input("New Title (leave blank to keep the current title): ").strip()
        new_status = input("New Status (leave blank to keep the current status): ").strip()
        if new_status:
            utils.validate_status(new_status)    
        new_description = input("New Description (leave blank to keep the current description): ").strip()
        new_due_date = input("New Due Date (YYYY-MM-DD) (leave blank to keep the current due date): ").strip()
        if new_due_date:
            utils.validate_date(new_due_date)
        task_to_update.update_details(
            title=new_title if new_title else task_to_update.title, 
            description=new_description if new_description else task_to_update.description,
            due_date=new_due_date if new_due_date else task_to_update.due_date,
            status=new_status if new_status else task_to_update.status
        )
        print("Task updated successfully.")
        main()  
    except ValueError as e:
        print(e)

def Delete_task():
    task_id = input("Please Enter the Task ID you want to Delete: ").strip()
    try :
        task_to_delete = find_task_by_id(task_id)
        tasks.remove(task_to_delete)
    except ValueError as e:
        print(e)
    
def write_in_file():
    try:
        if tasks :
            with open('tasks.json', 'w') as f:
                        json.dump([task.__dict__ for task in tasks],f)
            print("tasks saved to the file :)")
    except IOError as e :
        print("error while writting in the file ",e)

def read_from_file():
  try:      
    with open('tasks.json', 'r') as f:
        json_tasks = json.load(f)
        for task_data in json_tasks:
            task_id = task_data.pop('task_id', None)
            if 'priority' in task_data :
                task = UrgentTask(**task_data)
            else :
                task = Task(**task_data)
            task.task_id = task_id
            tasks.append(task)

  except ValueError as e :
      print(e)


def search_by_status():
  try:
    status = input("Enter the status to filter tasks: ").strip().lower()
    utils.validate_status(status)
    for task in tasks:
        if task.status == status:
            task.display()    
  except ValueError as e:
    print(e)

def main():
    while True :  
        try :
            menu()
            choice = input("Enter your choice: ")
            match choice:
                case '1':
                    add_task()
                case '2':
                    view_tasks()
                case '3':
                    update_task()
                case '4':
                    Delete_task()
                case '5':
                    search_by_status()
                case '6':
                    write_in_file()
                    exit()
                case _:
                    raise ValueError()          
        except ValueError:
            print("Invalid Value , please Enter a number from the list.")


read_from_file()
main()
2