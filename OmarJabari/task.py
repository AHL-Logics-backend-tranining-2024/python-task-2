from datetime import date

class Task:
    id_counter = 1
    def __generate_id(self):
        TaskID = Task.id_counter
        Task.id_counter += 1
        return TaskID
    def __init__(self, title, description, due_date, status="InProgress"):
        self.task_id = self.__generate_id()
        self.title = title
        self.description = description
        self.due_date = date.fromisoformat(due_date)
        self.status = status

    def _parse_date(self, due_date):
        return date.fromisoformat(due_date)


    def update_details(self, title, description, due_date, status):
        if title:
            self.title = title
        if description:
            self.description = description
        if due_date:
            self.due_date = self._parse_date(due_date)
        if status:
            self.status = status

    def display(self):
        return (f"TaskID : {self.task_id}\n "
                f"Title : {self.title}\n"
                f"Description : {self.description}\n "
                f"Due Date : {self.due_date}\n"
                f"Status : {self.status}\n ")


class UrgentTask(Task):
    def __init__(self , priority ,title, description, due_date, status="InProgress"):
       super().__init__(title , description , due_date , status)
       self.priority = priority

    def display(self):
        Father_Display = super().display()
        return Father_Display + "Priority : " + self.priority + "\n"




