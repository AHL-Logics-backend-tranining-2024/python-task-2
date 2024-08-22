import json
import uuid
from datetime import datetime
from enum import Enum
from Task import Task, UrgentTask, Status, Priority
from utils import get_valid_input

class TaskManager:
    _instance = None

    """Class to manage tasks including adding, viewing, updating, and deleting."""

    def __new__(cls, *args, **kwargs):
        """
        Ensure only one instance of TaskManager is created.
        """
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, data_file='data.json'):
        """
        Initialize the TaskManager with a specified data file.
        
        Parameters:
        - data_file: The path to the JSON file storing task data.
        """
        if not hasattr(self, 'initialized'):  # Prevent reinitialization
            self.data_file = data_file
            self.tasks = []
            self.urgent_tasks = []
            self.load_tasks()
            self.initialized = True  # Mark as initialized

    def load_tasks(self):
        """Load tasks from the JSON data file into the manager."""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                for item in data:
                    status = Status[item['status']]
                    if 'priority' in item:
                        priority = Priority[item['priority'].capitalize()]
                        task = UrgentTask(
                            title=item['title'],
                            description=item['description'],
                            due_date=item['due_date'],
                            status=status,
                            priority=priority
                        )
                        self.urgent_tasks.append(task)
                    else:
                        task = Task(
                            title=item['title'],
                            description=item['description'],
                            due_date=item['due_date'],
                            status=status
                        )
                        self.tasks.append(task)
        except FileNotFoundError:
            print(f"File {self.data_file} not found. Starting with an empty task list.")
        except json.JSONDecodeError:
            print("Error decoding JSON data. Starting with an empty task list.")

    def save_tasks(self):
        """Save the current tasks back to the JSON data file."""
        data = []
        for task in self.tasks + self.urgent_tasks:
            task_data = {
                'title': task.title,
                'description': task.description,
                'due_date': task.due_date.strftime('%Y-%m-%d'),
                'status': task.status.name
            }
            if isinstance(task, UrgentTask):
                task_data['priority'] = task.priority.name
            data.append(task_data)

        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)

    def add_task(self):
        """Prompt the user to add a new task, either regular or urgent."""
        title = get_valid_input("Enter the task title: ")
        description = get_valid_input("Enter the task description: ")
        due_date = get_valid_input("Enter the due date (YYYY-MM-DD): ")
        status_input = get_valid_input("Enter the status (InProgress/Completed): ")
        status = Status[status_input]

        is_urgent_input = get_valid_input("Is this an urgent task? (yes/no): ").lower()
        if is_urgent_input in ['yes', 'y']:
            priority_input = get_valid_input("Enter the priority (Low/Medium/High): ").capitalize()
            priority = Priority[priority_input]
            task = UrgentTask(title, description, due_date, status, priority)
            self.urgent_tasks.append(task)
        else:
            task = Task(title, description, due_date, status)
            self.tasks.append(task)

        self.save_tasks()
        print("Task added successfully.")

    def view_tasks(self):
        """Display all regular and urgent tasks."""
        print("\nRegular Tasks:")
        for task in self.tasks:
            task.display()

        print("\nUrgent Tasks:")
        for task in self.urgent_tasks:
            task.display()

    def update_task(self):
        """Update the details of an existing task."""
        task_id = get_valid_input("Enter the ID of the task to update: ")
        task = self.find_task_by_id(task_id)

        if task:
            title = input("Enter the new title (leave blank to keep current): ")
            description = input("Enter the new description (leave blank to keep current): ")
            due_date = input("Enter the new due date (YYYY-MM-DD) (leave blank to keep current): ")
            status_input = input("Enter the new status (InProgress/Completed) (leave blank to keep current): ")
            status = Status[status_input] if status_input else None

            task.update_details(title, description, due_date, status)
            self.save_tasks()
            print("Task updated successfully.")
        else:
            print("Task not found.")

    def delete_task(self):
        """Delete a task by its ID."""
        task_id = get_valid_input("Enter the ID of the task to delete: ")
        task = self.find_task_by_id(task_id)

        if task:
            if isinstance(task, UrgentTask):
                self.urgent_tasks.remove(task)
            else:
                self.tasks.remove(task)
            self.save_tasks()
            print("Task deleted successfully.")
        else:
            print("Task not found.")

    def find_task_by_id(self, task_id):
        """Find a task by its ID."""
        for task in self.tasks + self.urgent_tasks:
            if str(task.id) == task_id:
                return task
        return None
    
    def search_by_status(self):
     try:
      status = input("Enter the status to filter tasks: ").strip().lower()
      
      for task in self.tasks + self.urgent_tasks:
        if task.status == status:
            print(task.display())    
     except ValueError as e:
      print(e)

def main_menu():
    """Display the main menu and handle user input."""
    
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. search Task (status)")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task_manager.add_task()
        elif choice == '2':    
            task_manager.view_tasks()
        elif choice == '3':
            task_manager.search_by_status()    
        elif choice == '4':
            task_manager.update_task()
        elif choice == '5':
            task_manager.delete_task()
        elif choice == '6':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

     


if __name__ == "__main__":
    main_menu()
