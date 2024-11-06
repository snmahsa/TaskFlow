import uuid
from datetime import datetime
class Task:
    def __init__(self, task_name: str, task_description: str):
        task_id =  str(uuid.uuid4())
        self.task_id = task_id
        self.name = task_name
        self.description = task_description
        self.status = False
        self.start_time = None
        self.end_time = None
        self.duration = 0

    def mark_done(self, start_time_str, end_time_str):
        self.status = True
        self.start_time = datetime.strptime(start_time_str, "%H:%M")
        self.end_time = datetime.strptime(end_time_str, "%H:%M")
        self.duration = (self.end_time - self.start_time).total_seconds() / 3600
        
    def __str__(self):
        return f"Task(ID:{self.id}, Name:{self.name},Status:{'Done' if self.status==True else 'Not Done'},Duration:{self.duration:.2f} hours)\n"

            