import re
from task_status import Status

def validate_date(date_str):
    while True:
        # date_str = input(date_str)
        if re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
            return date_str
        else:
            print("Invalid date format. Use YYYY-MM-DD. Please try again.")

def get_valid_input(inputt):
  while True:
        #user_input = input(inputt).strip()
        if inputt:
            return inputt
        else:
            print("Input cannot be empty. Please try again.")
 

def validate_status(status):
 valid_statuses = ['inProgress', 'completed']
 while True:
        # status = input("Enter status (InProgress or Completed): ").strip().lower()
        # if status in valid_statuses:
        #     return status
        if status.upper() in Status.__members__:
            return Status[status.upper()]
        
        else:
            print(f"Invalid status. Choose from {valid_statuses}. Please try again.")

def validate_priority(priority):
    valid_priorities = ['high', 'medium', 'low']
    while True:
        if priority in valid_priorities:
            return priority 
        print(f"Invalid priority. Choose from {valid_priorities}.")
        priority = input("Enter the priority (high/medium/low) ").strip().lower()
