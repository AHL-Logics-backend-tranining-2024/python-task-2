from datetime import datetime

def validate_date(date_str):  
    if not datetime.strptime(date_str, '%Y-%m-%d'):
            raise ValueError("Incorrect date format, should be YYYY-MM-DD. Please try again.")
    return True

def get_valid_input(prompt):
    if not prompt.strip():
        raise ValueError("value canor be empty , Please try again.")
    return True
                 
def validate_status(status):
    if status not in ["inprogress", "completed"]:
        raise ValueError("invalid status , status must be either 'InProgress'or 'Completed'")
    return True

def validate_priority(priority):
    if priority not in ["high", "medium", "low"]:
            raise ValueError("Invalid priority , priority must be  High , Medium or Low ")
    return True
