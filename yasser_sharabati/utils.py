import datetime
import json
from task import Task, UrgentTask


def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def get_valid_input(prompt):
    user_input = input(prompt).strip()
    if not user_input:
        raise ValueError("Input cannot be empty.")
    return user_input

def validate_status(status):
    status = status.lower() 
    if status not in ['inprogress', 'completed']:
        raise ValueError("Invalid status. Must be 'InProgress' or 'Completed'.")
    return True

def validate_priority(priority):
    priority = priority.lower() 
    if priority not in ['high', 'medium', 'low']:
        raise ValueError("Invalid priority. Must be 'High', 'Medium', or 'Low'.")
    return True

def save_tasks_to_file(tasks, urgent_tasks, filename='tasks.json'):
    all_tasks = {
        'tasks': [task.to_dict() for task in tasks],
        'urgent_tasks': [task.to_dict() for task in urgent_tasks]
    }
    with open(filename, 'w') as f:
        json.dump(all_tasks, f, indent=4)

def load_tasks_from_file(filename='tasks.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            tasks = [Task.from_dict(task_data) for task_data in data['tasks']]
            urgent_tasks = [UrgentTask.from_dict(task_data) for task_data in data['urgent_tasks']]
            return tasks, urgent_tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return [], []
