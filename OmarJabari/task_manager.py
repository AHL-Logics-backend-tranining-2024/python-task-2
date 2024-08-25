from task import Task, UrgentTask
from utils import validate_status, validate_date, validate_priority, get_valid_input
from user_authentication import authenticate , read_credentials , get_credentials
tasks = {}
urgent_tasks = {}

def addTask():
    title, description, dueDate = (
        get_valid_input(x) for x in ["Enter title: ", "Enter description: ", "Enter due date (YYYY-MM-DD): "]
    )
    dueDate = validate_date(dueDate)
    isUrgent = get_valid_input("Is this task urgent? (yes/no): ").lower() in ['yes', 'y', 'yeah', 'ye']
    if isUrgent:
        priority = get_valid_input("Enter priority [High, Medium, Low]: ")
        validate_priority(priority)
        task = UrgentTask(priority, title, description, dueDate)
        urgent_tasks[task.task_id] = task
    else:
        task = Task(title, description, dueDate)
        tasks[task.task_id] = task

def updateTask():
    taskID = int(get_valid_input("Enter taskID: "))
    task = tasks.get(taskID) or urgent_tasks.get(taskID)
    if not task:
        print("Task Not Found!")
        return

    TASK_UPDATED = {
        "title": get_valid_input("Enter new title: "),
        "description": get_valid_input("Enter New Description: "),
        "due_date": get_valid_input("Enter new DueDate (YYYY-MM-DD): "),
        "status": get_valid_input("Enter new status (InProgress, Completed): ")
    }

    try:
        validate_date(TASK_UPDATED['due_date'])
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    try:
        validate_status(TASK_UPDATED['status'])
    except ValueError:
        print("Invalid status. Please use 'InProgress' or 'Completed'.")
        return

    task.update_details(**TASK_UPDATED)
    print("Task Updated Successfully!")

def deleteTask():
    task_id = int(get_valid_input("Enter task ID to delete: "))

    if task_id in tasks:
        del tasks[task_id]
        print(f"Task with ID {task_id} has been deleted.")
    elif task_id in urgent_tasks:
        del urgent_tasks[task_id]
        print(f"Urgent Task with ID {task_id} has been deleted.")
    else:
        print("Task not found.")

def displayTask(task):
    task_details = {
        'Task ID': task.task_id,
        'Title': task.title,
        'Description': task.description,
        'Due Date': task.due_date,
        'Status': task.status,
    }

    if isinstance(task, UrgentTask):
        task_details['Priority'] = task.priority

    for key, value in task_details.items():
        print(f"{key}: {value}")
    print("\n")

def displayTasks():
    if not tasks and not urgent_tasks:
        print("No tasks to display.")
        return

    print("\nRegular Tasks:")
    for task in tasks.values():
        displayTask(task)

    print("\nUrgent Tasks:")
    for task in urgent_tasks.values():
        displayTask(task)


def main_menu():
    credentials = read_credentials()

    while True:
        username, password = get_credentials()
        if authenticate(username, password, credentials):
            print("Authentication successful, Hi!")
            break
        else:
            print("Authentication failed, please try again.")

    while True:
        print("\nTask Manager Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = get_valid_input("Enter your choice (1-5): ")

        match choice:
            case '1':
                addTask()
            case '2':
                displayTasks()
            case '3':
                updateTask()
            case '4':
                deleteTask()
            case '5':
                print("Exiting Task Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
