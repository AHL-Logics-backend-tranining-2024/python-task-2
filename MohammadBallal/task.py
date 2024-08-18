class Task:
    def __init__(self,task_id,title,description,due_date,status) :
        #Initialize the attributes
        self.task_id= task_id
        self.title= title
        self.description= description
        self.due_date= due_date
        self.status=status
    
    #Define update_datails method for updating tasks details
    def update_datails(self, title= None, description= None, due_date= None, status= None):
        #using if statment to update details if provided
        if title:
            self.title= title
        if description:
            self.description= description
        if due_date:
            self.due_date= due_date
        if status:
            self.status= status

    #Define display method for returning thhe task details as string    
    def display(self):
        return(f" Title: {self.title}\n Description: {self.description}\n Due Date: {self.due_date}\n Status: {self.status}")




#Define UrgentTask which inherits from Task class
class UrgentTask(Task):
    def __init__(self, task_id, title, description, due_date, status, priority):
        super().__init__(task_id, title, description, due_date, status)
        self.priority= priority
    #Define diplay method for returning the Task class's display and priority as string
    def display(self):
        return(f" {super().display}\n Priority: {self.priority}")
    

