from task import Task, UrgentTask
from utils import validate_date, get_valid_input, valid_priority ,validate_status


regularTasks= []
urgentTasks= []

def add_task():
    #using get_valid_input for all user inputs to validate it
    title= get_valid_input("What is the task title? : ")
    description= get_valid_input("Just a little description for the task here please : ")
    due_date= get_valid_input("Enter task due date (DD/MM/YYYY)")
    #validate date format
    validate_date(due_date)
    status= get_valid_input("Enter task status ( Completed || InProgress )")
    #validate status 
    validate_status(status)
    #check if the task is urgent or not to know where to store it 
    isUrgent= get_valid_input("Is this task urgent (please write : yes || no) :  ")
    if isUrgent == "yes" :
        priority= get_valid_input("Enter task priority ( High || Medium || Low ) : ")
        #validate priority
        valid_priority(priority)
        task= UrgentTask(title,description,due_date,status,priority)
        urgentTasks.append(task)
    else :
        task= Task(title,description,due_date,status)
        regularTasks.append(task)
    
    print("TASK ADDED SUCCESSFULLY")

