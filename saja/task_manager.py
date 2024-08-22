import json
import uuid
from datetime import datetime
from enum import Enum
from Task import Task, UrgentTask, Status, Priority



class TaskManager:
    """Class to manage tasks including adding, viewing, updating, and deleting."""

    def __init__(self,data_file='data.json'):
     """
        Initialize the TaskManager with a specified data file.

        Parameters:
        - data_file: The path to the JSON file storing task data.
     """
     self.data_file = data_file
     self.tasks = []
     self.urgent_tasks = []
     self.load_tasks()


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
               



                







    


