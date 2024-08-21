import uuid
from enum import Enum
from datetime import datetime

class Status(Enum):
    """Enum to represent the status of a Task."""
    InProgress = "InProgress"
    Completed = "Completed"


class Task:
    """Class to represent a Task with a title, description, due date, and status."""
 
    def __init__(self,title,description,due_date,status: Status):
        """
        Initialize a Task instance.

        Parameters:
        - title: The title of the task.
        - description: A brief description of the task.
        - due_date: The due date of the task in the format 'YYYY-MM-DD'.
        - status: The current status of the task, should be an instance of Status enum.
        """
        self.id=uuid.uuid4() # Generate a unique identifier for the task.
        self.title=title
        self.description=description
        self.due_date=self.validateDate( due_date) # Validate  the due date.
        self.status=status# save enum value

    def validateDate(self,date):
       
       """
        Validate the format of the due date.

        Parameters:
        - due_date: The due date as a string in 'YYYY-MM-DD' format.

        Returns:
        - A datetime object if the date is valid.

        Raises:
        - ValueError: If the due date is not in the correct format.
        """       
       try:
          return datetime.strptime(date, '%Y-%m-%d')  
       except ValueError:
          raise ValueError("Enter the date correctly")  


    def update_details(self,title=None,description=None,due_date=None,status=None):
        """
        Update the details of the task.

        Parameters:
        - title: The new title of the task (optional).
        - description: The new description of the task (optional).
        - due_date: The new due date of the task (optional).
        - status: The new status of the task (optional, must be an instance of Status enum).
        """
        if title is not None:
         self.title=title
        if description is not None:
         self.description=description
        if due_date is not None: 
         self.due_date=self.validateDate(due_date) # Validate and update the due date.
        if status is not None and isinstance(status,Status):# save enum value
         self.status=status

    def display (self):
       print(f"The task title: {self.title} with Id :{self.id} \n The Description : {self.description}\n The Date: {self.date} \n The Status : {self.status.name}") 

