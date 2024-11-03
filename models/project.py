from task import Task
class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = {}
        
    def add_task_to_project (self, task):
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
            for task in self.tasks:
                print(f"ID: {task.id}, Name: {task.name}, Status: {'Done' if task.done else 'Not Done'}")

