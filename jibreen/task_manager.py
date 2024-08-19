from utils import get_valid_input
from task_operations import *
from display import display_Header,display_menu


if __name__ == "__main__":
   load_tasks_from_json()
   # Display the header of the application
   display_Header()

   while True:
    # Display the menu options
    display_menu()
    print("******************************************************")

    # Get user choice for functionality
    value_number = input(" Choose a functionality:")
    print("******************************************************")

    try:
      match value_number:
       case "1":
        # Option to add a new task with priority check
        print("********************* Add Task ***********************\n")
        create_task_with_priority_check()
    
       case "2":
        # Option to view all tasks
        print("******************* View Tasks ***********************\n")
        Print_Task()
        print("******************************************************")

       case "3":
        # Option to update an existing task
        print("******************* Update Task *********************\n")
        getId = input("Enter the number to update: ").strip()
        updatedTask(getId)
    
       case "4":
        # Option to delete a task
        print("****************** Delete Task **********************\n")
        deleteId = input("Enter the number to delete: ").strip()
        deleteTask(deleteId)

       case "5":
        # Option to save tasks to a JSON file
        print("****************** Save Task To Json ****************\n")
        save_tasks_to_JSON_file()

       case "6":
        # Option to load tasks from a JSON file
        print("****************** Load Task From Json **************\n")
        load_tasks_from_json()

       case "7":
        # Option to search tasks by status or due date
        print("********* Search by data (or/and status) ************\n")
        status = input("Enter the status: ")
        date = input("Enter the date: ")
        search_by_status_or_due_date(status, date)

       case "8":
        # Option to exit the task manager
        print("Exiting Task Manager. Goodbye!")
        break

       case _:
        # Handle invalid number input
        raise ValueError("Invalid number selected")

    except ValueError as e:
        # Print only the error message for invalid input or operations
        print(e)  # Print only the error message
