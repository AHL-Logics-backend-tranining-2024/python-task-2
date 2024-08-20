# **Task Manager Console Application**

## **Task Manager Classes**

### **`Task` Class:**

- **Purpose:** Represents a basic task.

- **Methods:**
- `__init__(title, description, due_date, status)`: Initializes a task.
- `updated_details(title=None, description=None, due_date=None, status=None)`: Updates task details.
- `__str__()`: "Returns a string representation of the task.""

## **`UrgentTask` Class:**

- **Purpose:** Extends Task with a priority attribute.

- **Methods:**
- `__init__(title, description, due_date, status, priority)`: Initializes an urgent task.
- `__str__()`: Returns a string representation including priority.

## **Utility Functions**

- `validate_date(due_date)`: Ensures the due date is in YYYY-MM-DD format.
- `validate_priority(priority)`: Confirms priority is either high, medium, or low.
- `validate_status(status)`: Verifies status is in progress or completed.
- `get_valid_input(prompt)`: Prompts user input and checks it’s not empty.

## **Task Management Functions**

- `create_task(title, description, due_date, status, priority=None)`: Adds a new task `(regular or urgent)` to the list.
- `create_task_with_priority_check()`: Prompts user input to create tasks with optional priority.
- `is_duplicate_task(new_task)`: Checks if a task is already in the list.
- `find_task_by_id(task_list, task_id)`: Finds a task by its ID.
- `updatedTask(id)`: Updates a task’s details by ID.
- `deleteTask(id)`: Removes a task by ID.
- `save_tasks_to_JSON_file(file_name="tasks.json")`: Saves the current task list to a JSON file.
- `load_tasks_from_json(file_name="tasks.json")`: Loads tasks from a JSON file.
- `search_by_status_or_due_date(status=None, due_date=None)`: Searches tasks by `status, due date, or both`.
- `Print_Task()`: Prints all tasks or shows a message if none exist.

## **User Interface Functions**

- `display_Header()`: Prints a formatted header for the Task Manager Console App.
- `display_menu()`: Prints the main menu with options for task management.

## **Main Application**

- `main.py`: Runs the Task Manager Console Application.
  - `Imports`:
    - `get_valid_input` from `utils`.
    - All functions from task_operations.
    - `display_Header`, `display_menu` from `display`.
- `Main Loop`:
  - `Displays header` and `menu`.
  - Handles user input for `adding`, `viewing`, `updating`, `deleting`, `saving`, `loading`, and `searching tasks`.
  - Validates input and handles errors gracefully.
  - Exits on user command.
