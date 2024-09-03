class Task:
#one
    task_id=0
    title=""
    description=""
    due_date=""
    status=""

    def __init__(self,title,description,due_date,status):
        Task.task_id+=1
        self.task_id = Task.task_id
        self.title=title
        self.description=description
        self.due_date=due_date
        self.status=status

    def update_details(self,title,description,due_date,status):
        self.title=title
        self.description=description
        self.due_date=due_date
        self.status=status

    def display(self):
        print(f"id: {self.task_id}\ntitle: {self.title}\ndescription: {self.description}\ndue date: {self.due_date}\nstatus: {self.status}")

class UrgentTask(Task):

    priority=""

    def __init__(self, title, description, due_date,  status,priority):
        super().__init__(title, description, due_date, status)
        self.priority=priority












