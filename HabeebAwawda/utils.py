from datetime import datetime


def validate_date(date_str) -> str:
    while True:
        try:
            datetime.strptime(date_str, '%d-%m-%Y')
            return date_str
        except ValueError:
            date_str=input("Please enter a valid date format (DD-MM-YYYY): ")

def get_valid_input(prompt) -> str:
    while True:
            if prompt:
                return prompt
            else:
                prompt = input("Value Error occurred (value cannot be None): ")


def validate_status(status) -> str:
    while True:

            match status:
                case '1':
                    return 'in_progress'
                case '2':
                    return 'completed'
                case _:
                    status=input("please enter a valid status number: ")


def validate_priority(priority) -> str:
    while True:
        match priority:
            case '1':
                return 'low'
            case '2':
                return 'medium'
            case '3':
                return 'high'
            case _:
                priority=input("please enter a valid priority number: ")

def validate_urgency(value) -> bool:
    while True:
        match value:
            case 'yes':
                return True
            case 'no':
                return False
            case _:
                value=input("please enter 'yes' or 'no': ")









