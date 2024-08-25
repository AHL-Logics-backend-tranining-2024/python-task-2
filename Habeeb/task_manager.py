import task
import utils

urgenList=[]
normalList=[]
tasksList=[urgenList,normalList]


def add():
    try:
        is_urgent = input("is your task urgent?")
        title = utils.get_valid_input(input('what is the title of your task?'))
        description = utils.get_valid_input(input('what is the description of your task?'))
        due_date = utils.validate_date(input('what is the due date?'))
        status = utils.validate_status(input('what is the status of your task?'))
        if is_urgent:
            priority = utils.validate_priority(input("what is your priority level?"))
            urgentTask = task.UrgentTask(title, description, due_date, status, priority)
            tasksList.append(urgentTask)
            print("Your task has been added.")
            return
        normalTask = task.Task(title, description, due_date, status)
        tasksList.append(normalTask)
        print("Your task has been added.")
    except Exception as e:
        print(f"Error occurred : {type(e).__name__} ")

def view():
    try:
        print('Urgent Tasks:\n')
        for i in urgenList:
            print(i+'\n')
        print("\nNon Urgent Tasks:\n")
        for j in normalList:
            print(j+'\n')
    except Exception as e:
        print(f"Error occurred : {type(e).__name__} ")

def update(taskID):
    try:
        for i in tasksList:
            if taskID == i.task_id:
                if isinstance(i, task.UrgentTask):
                    i.priority = utils.get_valid_input(input('what is the new priority?'))

                i.title = utils.get_valid_input(input('what is the new title?'))
                i.description = utils.get_valid_input(input('what is the new description?'))
                i.due_date = utils.get_valid_input(input('what is the new due date?'))
                i.status = utils.get_valid_input(input('what is the new status?'))
                print("Your task has been updated.")
                return
    except Exception as e:
        print(f"Error occurred : {type(e).__name__} ")

def delete(taskID):
    try:
        for i in tasksList:
            if taskID == i.task_id:
                tasksList.remove(i)
                print("Your task has been deleted.")
                return
    except Exception as e:
        print(f"Error occurred : {type(e).__name__} ")

while True:
    print("#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*\n")
    print("1.Add\n2.View\n3.Update\n4.Delete\n5.Exit")

    choice = input("select the number of the function please: ")

    match choice:
        case "1":
            add()
        case "2":
            view()
        case "3":
            update(input("what is the task id you want to update? \nnote:you can view the tasks by inter 2 in the main menu" ))
        case "4":
            delete(input("what is the task id you want to delete? \nnote:you can view the tasks by inter 2 in the main menu"))
        case "5":
            print("Good Bye!!")
            break
        case _:
            print("make sure you input the correct number")

