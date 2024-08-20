from task import Task

class UrgentTask (Task) :
    def __init__(self, title, description, due_date, priority):
        super().__init__(title, description, due_date)  
        self.priority=priority
    


    def display(self):
        displayString = (super().display()+f"priority: {self.priority}\n"
           )
        return displayString
    
urgent_task = UrgentTask("Important Task", "Review ", "2024-08-05", "Medium")
# print(urgent_task.display())
