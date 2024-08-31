class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
    
    def update_details(self, title=None, description=None, due_date=None, status=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if due_date is not None:
            self.due_date = due_date
        if status is not None:
            self.status = status

    def display(self):
        return (f"Task ID: {self.task_id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Due Date: {self.due_date}\n"
            f"Status: {self.status}")


class UrgentTask(Task):
    def __init__(self, task_id, title, description, due_date, status, priority):
        self.priority = priority
        super().__init__(task_id, title, description, due_date, status)
    
    def display(self):
        return super.display() + f"\nPriority: {self.priority}"
    
    def update_details(self, title=None, description=None, due_date=None, status=None, priority=None):
        super().update_details(title, description, due_date, status)
        if priority is not None:
            self.priority = priority


    
        