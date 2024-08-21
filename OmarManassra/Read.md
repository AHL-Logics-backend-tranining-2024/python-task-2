Task Manager Projecr:
**Overview
The Task Manager Console Application is a Python-based tool designed to help users manage their tasks efficiently through a command-line interface. This project demonstrates the use of essential Python programming concepts, including functions, classes, modules, exception handling, and object-oriented principles like encapsulation, inheritance, and polymorphism.

**Features
- Add Task: Input and save new tasks with details such as title, description, and due date.
- View Tasks: Display all tasks with their ID, title, description, due date, and status.
- Update Task: Modify details of existing tasks, including title, description, due date, and status.
- Delete Task: Remove tasks from the list based on their ID.



**How to Run
1. Clone the repository.
2. Navigate to the project directory.
3. Run the `task_manager.py` script:
   python task_manager.py



  First Creating the task file:
  Create Class task for normal tasks and intilize the task ID to Zero and incremented for each task created and build the constroucter (__inti__) and define the other Attributes 
  for method it contain two method (update,Display)
  
  Second Utils File:
  The file contain four function that are used to check the validity of some Inputs and if there is any Exception i let the function raise a ValueException with a massege relate to that error 

  Third file is Task Manager:
  Conatin a List of some choices to let the User choice the thing he want from (adding,deleting,etc...)tasks

 In each opreation of Input I call the Function of Exception Handling from utils module to check if there any Exception in the code 

