from task import Task, UrgentTask
from utils import validate_date, get_valid_input, valid_priority ,validate_status


regularTasks= {}
urgentTasks= {}

def add_task():
    #using get_valid_input for all user inputs to validate it
    title= get_valid_input("What is the task title? : ")
    description= get_valid_input("Just a little description for the task here please : ")
    due_date= get_valid_input("Enter task due date (DD/MM/YYYY)")
    #validate date format
    validate_date(due_date)
    #check if the task is urgent or not to know where to store it 
    isUrgent= get_valid_input("Is this task urgent (please write : yes || no) :  ").lower() #To reduce user input errors
    if isUrgent == "yes" :
        priority= get_valid_input("Enter task priority ( High || Medium || Low ) : ").lower()
        #validate priority
        valid_priority(priority)
        task= UrgentTask(title,description,due_date,priority)
        urgentTasks[task.task_id] = task
    else :
        task= Task(title,description,due_date)
        regularTasks[task.task_id] = task
    
    print("TASK ADDED SUCCESSFULLY")


def view_tasks():
    #Check if there any reguler tasks stored 
    if regularTasks:
        #Display every single task by display method from Task class
        for task in regularTasks.values():
            print(f"{task.display()}\n")
            
    else:
        print("There is no reguler tasks here")
    #Check if there any urgent task stored 
    if urgentTasks:
        for task in urgentTasks.values():
            print(f"{task.display()}\n")
    else:
        print("There is no urgent tasks here")


def update_task():
    #Make all tasks in one place 
    allTasks= {**regularTasks, **urgentTasks}
    taskId= int(get_valid_input("Enter task ID you need to update : "))
    taskUpdate = allTasks.get(taskId)
    

    if taskUpdate:
        new_taskTitle= input("Enter the new task title : ")
        new_taskDescription= input("Enter the new task description : ")
        new_taskDueDate= input("Enter the new due date(DD/MM/YYYY) : ")
        if new_taskDueDate:      
            validate_date(new_taskDueDate)
        new_taskStatus= input("Enter the new status( Completed || InProgress ) : ").lower() #to make sure not getting value error
        if new_taskStatus:
            validate_status(new_taskStatus)
        
        taskUpdate.update_details(new_taskTitle,new_taskDescription,new_taskDueDate,new_taskStatus)
        print("Task updated")


    else:
        print("Task not found")



def delete_task():
    taskId= int(get_valid_input("Enter task ID you need to delete : "))
    if taskId in regularTasks:
        del regularTasks[taskId]  #Remove from regular tasks
        print("Regular task deleted successfully.")
    elif taskId in urgentTasks:
        del urgentTasks[taskId]  #Remove from urgent tasks
        print("Urgent task deleted successfully.")
    else:
        print("Task not found.")
    




#Task manager menu 
while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Select an option (1-5): ")
    
    match choice:
        case '1':
            add_task()
        case '2':
            view_tasks()
        case '3':
            update_task()
        case '4':
            delete_task()
        case '5':
            print("Exiting Task Manager.")
            break
        case _:
            print("Invalid choice. Please select a valid option.")
    
