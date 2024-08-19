
#using some handling functions from  utils file
from utils import validate_date,validate_priority,validate_status

# Create module is Task
class Task:  
    _id_counter = 1 # Class-level counter for generating unique task IDs
    def __init__(self, title, description, due_date, status):
        """
        Initializes a new Task with the given details.
        
        :param title: Title of the task
        :param description: Description of the task
        :param due_date: Due date of the task (must be validated)
        :param status: Current status of the task (must be validated)
        """
        self.task_id = Task._id_counter # Assign a unique ID to the task
        Task._id_counter += 1 # Increment the ID counter for the next task
        self.title = title # Set the title of the tas
        self.description = description # Set the description of the task
        self.due_date = validate_date(due_date) # Validate and set the due date
        self.status = validate_status(status) # Validate and set the status
    
    def updated_details(self, title=None, description=None, due_date=None, status=None):
         """
        Updates the details of the task. Only provided arguments are updated.
        
        :param title: New title for the task (optional)
        :param description: New description for the task (optional)
        :param due_date: New due date for the task (optional, must be validated)
        :param status: New status for the task (optional, must be validated)
        """
         
         self.title = title if title is not None else self.title
         self.description = description if description is not None else self.description
         self.due_date = validate_date(due_date) if due_date is not None else self.due_date
         self.status = validate_status(status) if status is not None else self.status

    def __str__(self):
       """
        Returns a string representation of the task.
        
        :return: String representation of the task
       """
       return (
        f"Task ID: {self.task_id}\n"
        f"Title: {self.title}\n"
        f"Description: {self.description}\n"
        f"Due Date: {self.due_date}\n"
        f"Status: {self.status}\n"
       )


#create module is Urgent task [Task + one property]
class UrgentTask(Task):
    def __init__(self, title, description, due_date, status, priority):
        """
        Initializes a new UrgentTask with additional priority details.
        
        :param title: Title of the task
        :param description: Description of the task
        :param due_date: Due date of the task (must be validated)
        :param status: Current status of the task (must be validated)
        :param priority: Priority level of the urgent task (must be validated)
        """
        super().__init__( title, description, due_date, status) # Call the parent constructor
        self.priority = validate_priority(priority) # Validate and set the priority

    
    def __str__(self):
        """
        Returns a string representation of the urgent task, including priority.
        
        :return: String representation of the urgent task
        """
        return (
          f"{super().__str__()}"  # Include the string representation from the parent class
          f"Priority: {self.priority}")
