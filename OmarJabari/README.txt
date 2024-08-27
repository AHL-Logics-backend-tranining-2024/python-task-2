Hi it's Omar Jabari 

TASK MANAGER PROJECT ..............
..
.
Simple to handle tasks , urgentTasks  The functionality we have is to :
1- AddTask
2- Show Tasks
3- Update Tasks
4- Delete Tasks
5- Simple User Authentication with read from a file to achieve it .

...
Short explain :

addTask() : to add tasks or urgentTask based on userInput .

updateTask() : To update an existing task Based On taskID .

deleteTask() : To remove a Task using taskID .

displayTasks() : to display all the existing tasks with the details . 

displayTask(task) : to display an existing specific task with the details .

authenticate_user() : read the username and password from a file and match it to userinput if matched : pass else : failed

validate_date(date_str) : Validates the date format to ensure it matches YYYY-MM-DD , and error handling

get_valid_input(x) : Gets input from the user and checks if it’s empty.  If no input is given , and error handling

validate_status(status) : Checks if the task status is valid, either 'InProgress' or 'Completed' and .. error handling


validate_priority(priority) : Ensures that the priority entered by the user is one of 'High', 'Medium', or 'Low' , and errorhandling


main_menu() :  It displays options to the user .

