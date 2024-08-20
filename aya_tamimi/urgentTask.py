from task import Task

class UrgentTask(Task):

    def __init__(self , priority , title ,description , due_date , status) :
        super().__init__(title, description ,due_date ,status)
        self.priority = priority
    

    def display(self):
         super().display()
         print(f"Priority    : {self.priority}")


