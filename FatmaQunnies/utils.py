from datetime import datetime
from task_status import Status

def validate_date(date_str):
      try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            return date_str 
      except Exception:
           return None
           
def get_valid_input(inputt):
    if inputt:
            return inputt
    else:
         return None
 

def validate_status(status):
 valid_statuses = ['inProgress', 'completed']
 if status.upper() in Status.__members__:
        return Status[status.upper()]
        
 else:
        return None

def validate_priority(priority):
    valid_priorities = ['high', 'medium', 'low']
    if priority in valid_priorities:
         return priority 
    else:
        return None
    
