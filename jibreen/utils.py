from datetime import datetime


def validate_date(due_date):
    """
    Validates if the given due date is in the correct format.

    :param due_date: Date string to validate (format: YYYY-MM-DD)
    :return: The validated due date string if format is correct
    :raises ValueError: If the date format is incorrect
    """
    try:
      # Try to parse the date using the specified format
      datetime.strptime(due_date, '%Y-%m-%d')
      return due_date
    except ValueError:
      # Raise an error if the format is incorrect
      raise ValueError("The format is incorrect. Please use YYYY-MM-DD.")



def validate_priority(priority):
     """
     Validates the priority level, ensuring it is one of 'high', 'medium', or 'low'.

     :param priority: Priority level to validate
     :return: Normalized priority level (lowercase)
     :raises ValueError: If the priority level is invalid
     """
     match priority.lower():  # Ensure the status is case-insensitive
        case "high":
            return "high"
        case "medium":
            return "medium"
        case "low":
            return "low"
        case _:
            # Raise an error if the priority is not recognized
            raise ValueError("The priority is invalid")
         

def validate_status(status):
     """
     Validates the status, ensuring it is one of 'in progress' or 'completed'.

     :param status: Status to validate
     :return: Normalized status (capitalized)
     :raises ValueError: If the status is invalid
     """
     normalized_status = status.lower()
     match normalized_status:  # Ensure the status is case-insensitive
            case "in progress":
                return "In Progress"
            case "completed":
                return "Completed"
            case _:
                # Raise an error if the status is not recognized
                raise ValueError("The Status is invalid")
         


def get_valid_input(prompt):
    """
    Prompts the user for input and ensures it is not empty.

    :param prompt: The prompt message to display
    :return: The user input if it is not empty
    :raises ValueError: If the input is empty
    """
    value = input(prompt).strip() # Get and trim the user input
    if not value:
        # Raise an error if the input is empty
        raise ValueError("Input cannot be empty")
    return value