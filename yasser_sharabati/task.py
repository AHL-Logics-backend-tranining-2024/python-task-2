import json
import uuid

class Task:

    def __init__(self, title, description, due_date, status='InProgress'):
        self.task_id = uuid.uuid4()

        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def update_details(self, title=None, description=None, due_date=None, status=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if due_date:
            self.due_date = due_date
        if status:
            self.status = status

    def display(self):
        return f"[{self.task_id}] {self.title}: {self.description} (Due: {self.due_date}, Status: {self.status})"

    def to_dict(self):
        return {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data['title'],
            description=data['description'],
            due_date=data['due_date'],
            status=data['status'],
            task_id=data['task_id']
        )


class UrgentTask(Task):
    def __init__(self, title, description, due_date, priority, status):
        super().__init__(title, description, due_date, status)
        self.priority = priority

    def display(self):
        return f"[{self.task_id}] {self.title}: {self.description} (Due: {self.due_date}, Status: {self.status}, Priority: {self.priority})"

    def to_dict(self):
        data = super().to_dict()
        data['priority'] = self.priority
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data['title'],
            description=data['description'],
            due_date=data['due_date'],
            priority=data['priority'],
            status=data['status'],
            task_id=data['task_id']
        )
