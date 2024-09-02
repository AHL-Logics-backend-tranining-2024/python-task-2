
from datetime import datetime


def validate_date(date_str):
    if not isinstance(date_str, str):
        raise TypeError("Date should be a string.")


    date_parts = date_str.split('-')

    if len(date_parts) == 3:
        year = date_parts[0]
        month = date_parts[1].zfill(2)
        day = date_parts[2].zfill(2)
        date_str = f"{year}-{month}-{day}"

    try:

        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect date format. Expected format is YYYY-MM-DD.")

    return date_str

def get_valid_input(crab):
    value = input(crab)
    if not value :
        raise  ValueError("Can't be Empty , Add Crab ! )) ")
    return value

def validate_status(status):
    valid_status = {'InProgress', 'Completed'}
    if status not in valid_status:
        raise ValueError("Status Is Not Valid , Should be only InProgress || Completed")

def validate_priority(priority):
    valid_priority = {"High" , "Medium" , "Low"}
    if priority not in valid_priority:
        raise ValueError("Invalid priority")