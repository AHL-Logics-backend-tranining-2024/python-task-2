# **Task Manager Console Application**

## **Getting Started**

### **Setup**

1. **Clone the Main Repository:**
   ```bash
   git clone https://github.com/AHL-Logics-backend-tranining-2024/python-task-2
   cd python-task-2

2. **Create a New Branch:**
   Each intern should create a new branch for their individual project. The branch name should include your name or identifier:
   `git checkout -b <intern-name>-python-2-task`

3. **Create a New Folder:**
   Inside your branch, create a new folder to represent your project:
   ```
   mkdir <intern-name>
   cd <intern-name>
   ```

## **Project Overview**

The Task Manager Console Application is a Python-based tool designed to help users manage their tasks efficiently through a command-line interface. This project will help you practice essential Python programming concepts including functions, classes, modules, and exception handling, while exploring object-oriented principles like encapsulation, inheritance, and polymorphism.

## **Features**

- **Add Task:** Input and save new tasks with details such as title, description, and due date.
- **View Tasks:** Display all tasks with their ID, title, description, due date, and status.
- **Update Task:** Modify details of existing tasks, including title, description, due date, and status.
- **Delete Task:** Remove tasks from the list based on their ID.

## **File Descriptions**

### **`task.py`**

**Purpose:** This module defines the core classes for managing tasks.

- **`Task` Class:** 
  - **Attributes:**
    - `task_id`: A unique identifier for the task (auto-generated).
    - `title`: The title or name of the task.
    - `description`: A detailed description of the task.
    - `due_date`: The date by which the task should be completed (in YYYY-MM-DD format).
    - `status`: The current status of the task (e.g., 'InProgress', 'Completed').
  - **Methods:**
    - `update_details()`: Update task details such as title, description, due date, and status.
    - `display()`: Return a string representation of the task's details.

- **`UrgentTask` Class:** 
  - Inherits from `Task` and adds:
    - **Attributes:**
      - `priority`: The urgency level of the task (e.g., 'High', 'Medium', 'Low').
    - **Methods:**
      - `display()`: Extends the base `display` method to include the priority of the task.

### **`utils.py`**

**Purpose:** This module contains utility functions to support the task management operations.

- **`validate_date(date_str)`**: Validates the format of the date input (e.g., YYYY-MM-DD). Raises a ValueError if the format is incorrect.
- **`get_valid_input(prompt)`**: Prompts the user for input and ensures it is not empty. Raises a ValueError if the input is empty.
- **`validate_status(status)`**: Validates that the status is either 'InProgress' or 'Completed'. Raises a ValueError if the status is invalid.
- **`validate_priority(priority)`**: Validate that the priority is one of 'High', 'Medium', or 'Low'. Raises a ValueError if the priority is invalid.

### **`task_manager.py`**

**Purpose:** This is the main script that provides the user interface for interacting with the task manager.

- **Functionality:**
  - Provides a command-line interface for users to interact with the application.
  - Displays a menu with options to add, view, update, or delete tasks.
  - Utilizes the `Task` and `UrgentTask` classes and utility functions to manage tasks.
  
- **Explanation:**
    1. Add Task:
       1. Users are prompted to enter details for a new task. They are also asked if the task is urgent (e.g `is_urgent (bool): Yes, YES, YeS, NO, No, o ... etc are considered as a vlid input`).
       2. If the task is urgent, the UrgentTask class is used to create the task with a priority level.
       3. Otherwise, a regular Task is created.
    2. View Tasks:
       1. This function displays all tasks and urgent tasks separately.
    3. Update Task:
       1. Users can update details for any task. The function finds the task by its ID and updates its attributes. It also validates date and status if provided.
    4. Delete Task:
       1. Users can delete a task by its ID. The task is removed from the list of tasks and urgent tasks.
    5. Main Menu:
       1. Provides a command-line interface for users to select options to add, view, update, or delete tasks

## **Guidelines**

1. **Code Organization:** Organize your code into different modules for clarity and maintainability. 
2. **Exception Handling:** Implement error handling to manage invalid inputs, operations on non-existent tasks, and potential file I/O errors.
3. **Documentation:** Comment your code thoroughly to explain the purpose and functionality of each class and method, please create a README file within your folder project.
4. **Submission:** 
   1. Work within your own branch and folder in the cloned repository.
   2. Create a Pull Request: Once you have completed your work, push your changes in your branch to the repository and create a pull request. Ensure your pull request includes a description of the changes and any relevant details.
   3. Engage in discussions with peers and mentors for feedback and improvement.

## **Optional Extensions**

- **Data Persistence:** Add functionality to save and load tasks from a file using JSON or CSV formats.
- **User Authentication:** Implement user authentication to handle tasks for different users.
- **Task Search:** Add search features to filter tasks by status or due date.

