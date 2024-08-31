import datetime

def validate_date(date_str: str):
    try:
        # tries to parse the string to a datetime, if not possible thorugh exception
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Date '{date_str}' is not in the correct format (YYYY-MM-DD).")
    
def get_valid_input(prompt: str):
    user_input = input(prompt).strip()  
    if user_input == "": 
        raise ValueError("The input is empty")
    return user_input

def validate_status(status):
    if status != "InProgress" and status != "Completed":
        raise ValueError(f"the status '{status}' provided is not recognized.")

def validate_priority(priority): 
    if priority not in ('High', 'Medium', 'Low'):
        raise ValueError(f"the priority '{priority}' provided is not recognized.")
