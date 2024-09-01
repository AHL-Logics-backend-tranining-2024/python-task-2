def display_Header():
 """
    Display the header for the Task Manager Console Application.
    
    This function prints a formatted header to the console,
    providing an introductory message for the Task Manager application.
 """
 header = """
 *****************************************************
 *                                                   *
 *  >>>>>>>>>> The Task Manager Console App <<<<<<<< *
 *                                                   *
 *****************************************************
 """

 print(header);


def display_menu():
 """
    Display the main menu options for the Task Manager.
    
    This function prints a formatted menu to the console,
    listing available functionalities that the user can choose
    from, including adding, viewing, updating, deleting tasks,
    saving/loading tasks, and searching tasks.
 """
 menu = """
***************** Task Manager Menu ******************
* Choose an option from the menu:                    *
*  1. Add Task                                       *
*  2. View Tasks                                     *
*  3. Update Task                                    *
*  4. Delete Task                                    *
*  5. Save Tasks                                     *
*  6. Load Tasks                                     *
*  7. Search by date or status                       *
*  8. Exist                                          *
******************************************************
 """

 print(menu)