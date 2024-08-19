from  utils import validate_date,get_valid_input,validate_status,validate_priority
from task import Task,UrgentTask

tasks_list=[]
def Add_task():
    """ Call the Exception Handling Functions in the other module at every step it should be called"""
    title=input("Enter the title")
    description=input("enter the description")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    validate_date(due_date)
    status = input("Enter status ('InProgress' or 'Completed'): ")
    validate_status(status)
    
    try:
        """ Check if its Urgant """
        isUrgant=input("enter if urgant or not (yes or no or Invalid)")
        if isUrgant in ["yes","no"]:
            priority = input("Enter priority ('High', 'Medium', 'Low'): ")
            validate_priority(priority)
            addUrgent= UrgentTask(priority,title,description,due_date,status)
            tasks_list.append(addUrgent)
        else:
            addtask=Task(title,description,due_date,status)
            tasks_list.append(addtask)
            """ Check if there any Exception in adding tasks to the task list"""
    except ValueError as e:
        print (e)

def View_Tasks():
    """ Display the tasks"""
    if tasks_list:
         for task in tasks_list:
            task.display()
    else:
        print ("No tasks added")

def Update_Task():
    taskId=int(input("Enter the task you want to update"))







    

def Delete_Task():
    taskId=int(input("Enter the task you want to delate "))
    for task in tasks_list:
        if taskId==task.task_id:
            tasks_list.remove(taskId)

def main():
    while True:
        """ Creating the List of choices to click the right one """
        print ("1.Add Task\n 2.View Tasks\n 3.Update Task\n 4.Delete Task\n  5.exit")
        Choice=input("Enter the choice ")
        match Choice:
            case "1":
                 Add_task()
            case "2":
                 View_Tasks()
            case "3":
                 Update_Task()
            case "4":
                 Delete_Task()
            case "5":
                 print ("Thanks For Using")
                 break 
            case _:
                  print ("Invalid")

main()
