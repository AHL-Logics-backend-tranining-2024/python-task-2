from utils import *
from task import *


tasks={}
def add():
    try:
        is_urgent = validate_urgency(input("is your task urgent?   yes | no: "))
        title = get_valid_input(input('what is the title of your task?'))
        description = get_valid_input(input('what is the description of your task?'))
        due_date = validate_date(input('what is the due date?   DD-MM-YYYY: '))
        status = validate_status(input('what is the status of your task?   in_progress (1) | completed (2): '))
        if is_urgent:
            priority = validate_priority(input("what is your priority level ?   low (1) | medium (2) | high (3): "))
            urgent_task = UrgentTask(title, description, due_date, status, priority)
            tasks[urgent_task.task_id] = urgent_task
            print("__________________________________________\nYour task has been added.")
            return
        task = Task(title, description, due_date, status)
        tasks[task.task_id] = task
        print("__________________________________________\nYour task has been added.")
    except Exception as e:
        print(f'Error:{type(e).__name__}')
def view():
    try:
        print('------------------\nUrgent Tasks:\n')
        for i in tasks.values():
            if isinstance(i,UrgentTask):
                i.display()
                print('+-+-+-+-+-+-+')

        print('-----------------------\nRegular Tasks:\n')
        for i in tasks.values():
            if not isinstance(i,UrgentTask):
                i.display()
                print('+-+-+-+-+-+-+')

        print('---------------------------------')
    except Exception as e:
        print(f'Error:{type(e).__name__}')
def update(taskID):
    try:
        for i in tasks.keys():
            if taskID == i:
                current_task = tasks[i]
                if isinstance(current_task,UrgentTask):
                    current_task.priority = validate_priority(input('what is the new priority?   low (1) | medium (2) | high (3): '))

                current_task.title = get_valid_input(input('what is the new title?'))
                current_task.description = get_valid_input(input('what is the new description?'))
                current_task.due_date = validate_date(input('what is the new due date?  DD-MM-YYYY: '))
                current_task.status = validate_status(input('what is the new status?   in_progress (1) | completed (2): '))
                print("-----------------------------------------\nYour task has been updated.")
                return
        print('-------------------------------\nTask ID does not exist.')
    except Exception as e:
        print(f'Error:{type(e).__name__}')
def delete(taskID):
    try:
        for i in tasks.keys():
            if taskID == i:
                del tasks[i]
                print("----------------------------\nYour task has been deleted.")
                return
        print('Task ID does not exist.')
    except Exception as e:
        print(f'Error:{type(e).__name__}')

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
            update(int(input("\nwhat is the task id you want to update? " )))
        case "4":
            delete(int(input("\nwhat is the task id you want to delete? ")))
        case "5":
            print("\n\nGood Bye!!")
            break
        case _:
            print("make sure you select a valid number, Try again: ")

