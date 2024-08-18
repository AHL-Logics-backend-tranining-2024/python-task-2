from datetime import date

class Task:
 
    counter = 0  
    def __init__(self, title, description, due_date):
        Task.counter += 1 
        self.task_id = Task.counter 
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = 'InProgress' #Default value

    def update_details(self, title=None, description=None, due_date=None):
        if title  is not None:
            self.title = title
        if description is not None:
            self.description = description
        if due_date is not None:
            self.due_date = due_date


    def display(self):
        displayString = (f"Task ID: {self.task_id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Due Date: {self.due_date}\n"
            f"Status: {self.status}")
        return displayString
    
    
task =Task("pythonTask","classes","2/4/2024")
task2 =Task("pythonTask2","classes","2/4/2024")
task3 =Task("pythonTask3","classes","2/4/2024")

print(task.display())
print(task2.display())
print(task3.display())