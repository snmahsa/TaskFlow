from models.task import Task
class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = {}
        
    def add_task (self, task):
        if isinstance(task, Task):
            self.tasks[task.task_id]=task
        else:
            raise TypeError("Only Task objects can be added.")
        
    def remove_task(self, task_id):
        del self.tasks[task_id]

    def get_task(self,task_id):
        if self.tasks[task_id]:
            return self.tasks[task_id]
        else:
            return None
        
    def list_tasks(self):
        if not self.tasks:
            print("No tasks available in this project.")
        else:
            for task_id, task in self.tasks.items():
                print(f"ID: {task_id}, Name: {task.name}, Status: {'Done' if task.status else 'Not Done'}", end=' ')
            if task.status:
                print(f", Duration: {task.duration}")
                print(f", Start time: {task.start_time}")
                print(f", End time: {task.end_time}")

