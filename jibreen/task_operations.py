from task import Task,UrgentTask
from utils import get_valid_input,validate_status,validate_date
import json
import os

# List to store task
tasks =[]

def create_task(title, description, due_date, status, priority=None):
    
    """
    Creates a new task (urgent or regular) and adds it to the task list.

    :param title: Title of the task
    :param description: Description of the task
    :param due_date: Due date of the task (must be validated)
    :param status: Current status of the task (must be validated)
    :param priority: Priority of the task (optional, only for UrgentTask)
    """

    # Create a new task based on whether priority is provided
    if priority:
        new_task = UrgentTask(title, description, due_date, status, priority)   
    else:
        new_task = Task(title, description, due_date, status)
    # Check if the task is a duplicate before adding it
    if not is_duplicate_task(new_task):
        tasks.append(new_task)
        print("Task added successfully!")
    else:
        print("Duplicate task. Not added.")
    
    # Print the details of the newly created task
    print(new_task)  # Print the task details
    print("******************************************************")


def create_task_with_priority_check():
    """
    Handles user input to create a task with or without priority.
    """
    try:
        # Get user input for task details
        title = get_valid_input("Please enter the title of the task: ")
        description = get_valid_input("Please enter the Description of the task: ")
        due_date = get_valid_input("Please enter the due date of the task (YYYY-MM-DD): ")
        status = get_valid_input("Please enter the status of the task (In Progress/Completed): ")

        # Check if the task is urgent and get priority if needed
        is_urgent = input("Is this task urgent (True/False)? ").strip().lower()
        if  is_urgent == "true":
            priority = input("Please enter the priority of the task (Low/Medium/High): ")
            print("******************************************************")
            create_task(title, description, due_date, status , priority)
        else:
            print("******************************************************")
            create_task(title, description, due_date, status) 
    except ValueError as e:
         # Handle any validation errors
         print(f"Error: {e}")


def is_duplicate_task(new_task):
    """
    Checks if the provided task already exists in the task list.

    :param new_task: Task object to check for duplication
    :return: True if a duplicate task is found, False otherwise
    """
    for task in tasks:
        if (task.title == new_task.title and
            task.description == new_task.description and
            task.due_date == new_task.due_date):
            return True
    return False

def find_task_by_id(task_list, task_id):
    """
    Finds a task in the list by its ID.

    :param task_list: List of tasks to search through
    :param task_id: ID of the task to find
    :return: Task with the specified ID or None if not found
    """
    return next((task for task in task_list if task.task_id == task_id), None)

def updatedTask(id):
    """
    Updates the details of a task identified by its ID.

    :param id: ID of the task to update (must be a string)
    """
    if isinstance(id, str):
        try:
            # Find the task by ID
            task = find_task_by_id(tasks, int(id))
            if task is None:
                print("Task not found")  
                return  # Exit if the task is not found          
        except ValueError:
            print("Invalid ID format")
            return  # Exit if the ID format is invalid 

        # Get updated details from user
        title = input("Update title: ").strip()
        description = input("Update description: ").strip()
        due_date = input("Update due date: ").strip()
        status = input("Update status: ").strip()

        print("******************************************************")
        # Update task details with provided values
        task.updated_details(
            title=title or None,
            description=description or None,
            due_date=due_date or None,
            status=status or None
        )
        
        # Print updated task details
        print("******************************************************")
        print("Task ID:", task.task_id)
        print("Title:", task.title)
        print("Description:", task.description)
        print("Due Date:", task.due_date)
        print("Status:", task.status)
        print("******************************************************")

def deleteTask(id):
    """
    Deletes a task identified by its ID from the task list.

    :param id: ID of the task to delete (must be a string)
    """
    if isinstance(id, str):
        try:
            # Convert ID to integer and find the task
            task_id = int(id)
            task = find_task_by_id(tasks, task_id)
            if task is None:
                print("Task not found")
                return # Exit if the task is not found          
        except ValueError:
            print("Invalid ID format")
            return  # Exit if the ID format is invalid   
    
    # Remove the found task from the list
    tasks.remove(task);
    print("******************************************************")
    print("Removed Successfully")
    print("******************************************************")


def save_tasks_to_JSON_file(file_name="tasks.json"):
  """
    Saves the current list of tasks to a JSON file.

    :param file_name: Name of the JSON file to save tasks (default is "tasks.json")
  """
  # Open the specified file in write mode
  with open(file_name, 'w') as file:
        # Serialize the tasks list to JSON and write to the file
        json.dump([task.__dict__ for task in tasks], file, indent = 4)
  print("******************************************************")
  print(f"Tasks saved to {file_name}.") # Confirmation message
  print("******************************************************")


def load_tasks_from_json(file_name = "tasks.json"):
    """
    Loads tasks from a JSON file into the current task list.

    :param file_name: Name of the JSON file to load tasks from (default is "tasks.json")
    """
    # Check if the file exists
    if not os.path.exists(file_name):
        print(f"No file named {file_name} found. Starting with an empty task list.")
        return

    # Open the specified file in read mode
    with open(file_name, 'r') as file:
         # Deserialize the JSON data into a list of task data
         task_list  = json.load(file);
         for task_data in task_list:
             # Extract and remove the task ID from the task data
             task_id = task_data.pop('task_id', None)

             # Create a Task or UrgentTask object based on the presence of 'priority' 
             if "priority" in task_data:
                 task = UrgentTask(**task_data)
             else:
                 task = Task(**task_data)
             task.task_id = task_id
             # Add the task to the list if it's not a duplicate
             if not is_duplicate_task(task):
              tasks.append(task);
    print(f"Loaded tasks from {file_name}.")
       

def search_by_status_or_due_date(status=None, due_date=None):
    """
    Searches for tasks based on status, due date, or both.

    :param status: Status of the tasks to search for (optional)
    :param due_date: Due date of the tasks to search for (optional, format: YYYY-MM-DD)
    """
    print("******************************************************")
    if status and not due_date:
        # Search by status only
        match_statement = [task for task in tasks if task.status.lower() == validate_status(status).lower()]
        if not match_statement:
            print(f"No tasks found with status '{status}'.")
        else:
            for task in match_statement:
                print(task)
                print("\n")

    elif not status and due_date:
        # Search by due date only
        try:
            valid_due_date = validate_date(due_date)
            match_statement = [task for task in tasks if task.due_date == valid_due_date]
        except ValueError as e:
            print(e) # Print validation error if due date is invalid
            return

        if not match_statement:
            print(f"No tasks found with due date '{due_date}'.")
        else:
            for task in match_statement:
                print(task)
                print("\n")

    elif status and due_date:
        # Search by both status and due date
        try:
            valid_due_date = validate_date(due_date)
            match_statement = [task for task in tasks if task.due_date == valid_due_date and task.status.lower() == validate_status(status).lower()]
        except ValueError as e:
            print(e)  # Print validation error if due date is invalid
            return

        if not match_statement:
            print(f"No tasks found with status '{status}' and due date '{due_date}'.")
        else:
            for task in match_statement:
                print(task)
                print("\n")

    else:
        # If neither status nor due date is provided, print all tasks
        Print_Task()
