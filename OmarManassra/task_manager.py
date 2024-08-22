from  utils import validate_date,get_valid_input,validate_status,validate_priority
from task import Task,UrgentTask
# Dictionory contains all the tasks 
tasks_dict = {}
def add_task():
    """ Call the Exception Handling Functions in the other module at every step it should be called"""
    title=input("Enter the title")
    description=input("enter the description")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    validate_date(due_date)
    status = input("Enter status ('InProgress' or 'Completed'): ")
    validate_status(status)
    try:
        """ Check if its Urgant """
        is_urgant=input("enter if urgant or not (True or False)")
        if is_urgant:
            priority = input("Enter priority ('High', 'Medium', 'Low'): ")
            validate_priority(priority)
            addUrgent= UrgentTask(priority,title,description,due_date,status)
            tasks_dict[addUrgent.task_id]=addUrgent
        else:
            addtask=Task(title,description,due_date,status)
            tasks_dict[addtask.task_id]=addtask
            """ Check if there any Exception in adding tasks to the task list"""
        
    except ValueError as e:
        print (e)

def view_tasks():
    """ Display the tasks"""
    if tasks_dict:
         for task in tasks_dict.values():
            task.display()
    else:
        print ("No tasks added")


def update_task():
    task_id=int(input("Enter the task you want to update"))
    title=input("Enter the title updated ")
    description=input("enter the description update")
    due_date = input("Enter due date (YYYY-MM-DD) update: ")
    validate_date(due_date)
    status = input("Enter status ('InProgress' or 'Completed'): update ")
    validate_status(status)
    if task_id in tasks_dict:
        task = tasks_dict[task_id]
        task.title = title
        task.description = description
        task.due_date = due_date
        task.status = status
        isUrgant=input("enter if urgant or not (True or False)")
        if isUrgant:
            priority = input("Enter updated priority ('High', 'Medium', 'Low'): ")
            validate_priority(priority)
            task.priority = priority
        
           
def delete_task():
    task_id=int(input("Enter the task you want to delate "))
    if task_id in tasks_dict:
        del tasks_dict[task_id]
        print ("task have been removed ")
    else:
        print ("No Task found ")

def main():
    while True:
        """ Creating the List of choices to click the right one """
        print ("1.Add Task\n 2.View Tasks\n 3.Update Task\n 4.Delete Task\n  5.exit")
        Choice=input("Enter the choice ")
        match Choice:
            case "1":
                 add_task()
            case "2":
                 view_tasks()
            case "3":
                 update_task()
            case "4":
                 delete_task()
            case "5":
                 print ("Thanks For Using")
                 break 
            case _:
                  print ("Invalid")

main()
