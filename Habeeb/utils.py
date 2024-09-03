from datetime import datetime


def validate_date(date_str) -> str:
    while True:
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            date_str=input("Please enter a valid date format (YYYY-MM-DD): ")

def get_valid_input(prompt) -> str:
    while True:
        try:
            if (prompt is not None):
                return prompt
            raise ValueError
        except ValueError:
            prompt=input("Value Error occurred (value cannot be None): ")

def validate_status(status) -> str:
    while True:
        try:
            if status in ("InProgress", "Completed"):
                return status
            raise ValueError
        except ValueError:
           status=input("Value Error occurred (status value should be 'InProgress' or 'Completed'): ")

def validate_priority(priority) -> str:
    while True:
        try:
            if priority in ("Low", "Medium", "High"):
                return priority
            raise ValueError
        except ValueError:
            priority=input("Value Error occurred (priority value should be 'Low' or 'Medium' or 'High'): ")









